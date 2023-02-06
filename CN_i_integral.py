# ===================================
# FEniCS code  
# ===================================
# Solution of elasticity problem (CN specimen) for calculating interation integral
# author: Xinyuan ZHAI (xinyuan.zhai@ensta-paris.fr)




from __future__ import division
from dolfin import *

import pandas as pd
import argparse
import math
import os
import shutil
import sympy
import sys
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# ----------------------------------------------------------------------------
# Parameters for DOLFIN and SOLVER 
# ----------------------------------------------------------------------------
set_log_level(LogLevel.INFO)  # log level
# set some dolfin specific parameters
info(parameters,True)
parameters["form_compiler"]["optimize"] = True
parameters["form_compiler"]["cpp_optimize"] = True
parameters["form_compiler"]["representation"] = "uflacs"

# -----------------------------------------------------------------------------
# parameters of the solvers
solver_u_parameters = {"nonlinear_solver": "newton",
                       "newton_solver": {"linear_solver": "mumps",
                                          "maximum_iterations": 100,
                                          "absolute_tolerance": 1e-8,
                                          "relative_tolerance": 1e-6,
                                          "report": True,
                                          "error_on_nonconvergence": True}}                              
# parameters of the PETSc/Tao solver used for the alpha-problem
tao_solver_parameters = {"maximum_iterations": 200,
                         "report": False,
                         "line_search": "more-thuente",
                         "linear_solver": "mumps",
                         "method": "tron",
                         "gradient_absolute_tol": 1e-8,
                         "gradient_relative_tol": 1e-8,
                         "error_on_nonconvergence": True}


# In[3]:


filename = "mesh/CN_ad"
#Read mesh
mesh = Mesh()
hdf = HDF5File(mesh.mpi_comm(), filename + ".h5", "r")
hdf.read(mesh, "/mesh", False)
ndim = mesh.topology().dim()

boundaries = MeshFunction("size_t", mesh,1)
hdf.read(boundaries, "/boundaries")

subdomains = MeshFunction("size_t", mesh,2)
hdf.read(subdomains, "/subdomains")

rename_subdomains = MeshFunction("size_t", mesh, 2)
rename_subdomains.set_all(0)
rename_subdomains.array()[subdomains.array()==1] = 1

dx = Measure("dx", domain=mesh, subdomain_data=rename_subdomains)

rename_boundaries = MeshFunction("size_t", mesh, 1)
rename_boundaries.set_all(0)
rename_boundaries.array()[boundaries.array()==2] = 2
rename_boundaries.array()[boundaries.array()==3] = 3


ds = Measure("ds", domain=mesh, subdomain_data=rename_boundaries)




plot(mesh)




#material
E = Constant(3000.0)
nu = Constant(0.35)
Gc = Constant(0.11)
ell = Constant(0.6)
ut = Constant(1.0)
k_ell = Constant(1e-6)




Id = Identity(ndim)

n = FacetNormal(mesh)

ex  = Constant((1.0, 0.0))

ey  = Constant((0.0, 1.0))

e1 = Constant((1.0,1.0))

kdelta = Constant((1.0, 0.0))

def u_x(u):
    return u.dx(0)

def utt(u):
    return grad(u).T

# -----------------------------------------------------------------------------
# Strain and stress and Constitutive functions of the damage model
# -----------------------------------------------------------------------------
# Strain and stress
def eps(v):
    return sym(grad(v))

def sigma_0(v):
    mu    = E/(2.0*(1.0 + nu))
    lmbda = E*nu/(1.0 - nu**2) # plane stress
    return 2.0*mu*eps(v) + lmbda*tr(eps(v))*Id

# Constitutive functions of the damage model
def w(alpha):
    return alpha

def a(alpha):
    return (1-alpha)**2

def sigma(u, alpha):
    return (a(alpha)+k_ell)*sigma_0(u)


# In[6]:


modelname = "CN_AT1_E3000_beta90"
meshname  = modelname+"-mesh.xdmf"

savedir   = "CN_isotropy_displacement/"+modelname+"/"

if MPI.rank(MPI.comm_world) == 0:
    if os.path.isdir(savedir):
        shutil.rmtree(savedir)

file = File(savedir + "facets.pvd")
file << rename_boundaries


# In[8]:


# Create function space for 2D elasticity + Damage
V_u     = VectorFunctionSpace(mesh, "Lagrange", 1, dim = 2)
V_alpha = FunctionSpace(mesh, "Lagrange", 1)

# Define the function, test and trial fields
u       = Function(V_u, name="Displacement")
du      = TrialFunction(V_u)
v       = TestFunction(V_u)
alpha   = Function(V_alpha, name="Damage")
dalpha  = TrialFunction(V_alpha)
beta    = TestFunction(V_alpha)




# Boundary conditions
g1 = Expression(("cos(80*pi/180)*t","sin(80*pi/180)*t"), t = 1, degree=0)
bc_u1 = DirichletBC(V_u, g1, boundaries, 2)
bc_u2 = DirichletBC(V_u, Constant((0.,0.)), boundaries, 3)
#bc_u2 = DirichletBC(V_u.sub(0), 0, boundaries, 3)
bc_u = [bc_u1, bc_u2]




#boundary condition for damage
#bc_a1 = DirichletBC(V_alpha, Constant(0.), boundaries, 2)
#bc_a2 = DirichletBC(V_alpha, Constant(0.), boundaries, 3)
#bc_alpha = [bc_a1, bc_a2]

#z = sympy.Symbol("z", positive=True)
#c_w = float(4 * sympy.integrate(sympy.sqrt(w(z)), (z, 0, 1)))

elastic_energy = 1./2.*inner(sigma(u, alpha), eps(u))*dx

# Weak form of elasticity problem
E_u  = derivative(elastic_energy,u,v)
# Writing tangent problems in term of test and trial functions for matrix assembly
E_du = derivative(E_u, u, du)

#dissipated_energy  = Gc/float(c_w)*(w(alpha)/ell + ell*inner(grad(alpha), grad(alpha)))*dx

#damage_functional = elastic_energy + dissipated_energy

# First and second directional derivative wrt alpha
#E_alpha = derivative(damage_functional,alpha,beta)
#E_alpha_alpha = derivative(E_alpha,alpha,dalpha)




# Variational problem for the displacement
problem_u = NonlinearVariationalProblem(E_u, u, bc_u, J=E_du)
# Set up the solvers                                        
solver_u  = NonlinearVariationalSolver(problem_u)
solver_u.parameters.update(solver_u_parameters)


# In[10]:


# --------------------------------------------------------------------
# Implement the box constraints for damage field
# --------------------------------------------------------------------
# Variational problem for the damage (non-linear to use variational inequality solvers of petsc)
# Define the minimisation problem by using OptimisationProblem class

#class DamageProblem(OptimisationProblem):

    #def __init__(self,f,gradf,alpha,J,bcs):
        #OptimisationProblem.__init__(self)
        #self.total_energy = f
        #self.Dalpha_total_energy = gradf
        #self.J_alpha = J
        #self.alpha = alpha
        #self.bc_alpha = bcs

    #def f(self, x):
        #self.alpha.vector()[:] = x
        #return assemble(self.total_energy)

    #def F(self, b, x):
        #self.alpha.vector()[:] = x
        #assemble(self.Dalpha_total_energy, b)
        #for bc in self.bc_alpha:
            #bc.apply(b)

    #def J(self, A, x):
        #self.alpha.vector()[:] = x
        #assemble(self.J_alpha, A)
        #for bc in self.bc_alpha:
            #bc.apply(A)

#damage_problem = DamageProblem(damage_functional,E_alpha,alpha,E_alpha_alpha,bc_alpha)

# Set up the solvers                                        
#solver_alpha  = PETScTAOSolver()
#solver_alpha.parameters.update(tao_solver_parameters)



#alpha_lb = interpolate(Expression("0.", degree=0), V_alpha)  # lower bound, set to 0
#alpha_ub = interpolate(Expression("1.", degree=0), V_alpha)  # upper bound, set to 1

#alpha_0 = interpolate(Expression("0.", degree=0), V_alpha)  # initial (known) alpha


# In[11]:


file_u = XDMFFile(MPI.comm_world, savedir+"/u.xdmf")
file_alpha = XDMFFile(MPI.comm_world, savedir+"/alpha.xdmf")
file_a = XDMFFile(MPI.comm_world, savedir+"/a.xdmf")
file_sigma = XDMFFile(MPI.comm_world, savedir+"/sigma.xdmf")

file_I = XDMFFile(MPI.comm_world, savedir+"/I_int.xdmf")
file_Ik1 = XDMFFile(MPI.comm_world, savedir+"/I_k1.xdmf")
file_Ik2 = XDMFFile(MPI.comm_world, savedir+"/I_k2.xdmf")

for file in [file_u,file_a,file_sigma,file_alpha, file_I, file_Ik1, file_Ik2]:
    file.parameters["flush_output"]=True
    file.parameters["rewrite_function_mesh"]=True


# In[12]:


load_multipliers  = np.linspace(0, 1, 2)

energies = np.zeros((len(load_multipliers),4))
iterations = np.zeros((len(load_multipliers),2))
force = np.zeros((len(load_multipliers),2))
# Numerical parameters of the alternate minimization
maxiteration = 2000
AM_tolerance = 1e-4





#Define auxiliry field for T-stress
mu = float(E/(2.0*(1.0 + nu)))
kappav = float((3.0-nu)/(1.0+nu))
Force = 1
d0 = 1
u_aux = Expression(["(-F*(kappa+1)/(pi*8*mu))*2.3*std::log(sqrt(x[0]*x[0]+x[1]*x[1])/d)- (F/(pi*4*mu))*sin(atan2(x[1], x[0]))*sin(atan2(x[1], x[0]))",
                    "(-F*(kappa-1)/(pi*8*mu))*atan2(x[1], x[0])+ (F/(pi*4*mu))*sin(atan2(x[1], x[0]))*cos(atan2(x[1], x[0]))"],
                    degree=2, mu=mu, kappa=kappav, F=Force,domain=mesh,d = d0)

sigmax = Expression((('-F*pow(cos(atan2(x[1], x[0])),3)/(pi*sqrt(x[0]*x[0]+x[1]*x[1]))','-F*pow(cos(atan2(x[1], x[0])),2)*sin(atan2(x[1], x[0]))/(pi*sqrt(x[0]*x[0]+x[1]*x[1]))'),
                ('-F*pow(cos(atan2(x[1], x[0])),2)*sin(atan2(x[1], x[0]))/(pi*sqrt(x[0]*x[0]+x[1]*x[1]))','-F*cos(atan2(x[1], x[0]))*pow(sin(atan2(x[1], x[0])),2)/(pi*sqrt(x[0]*x[0]+x[1]*x[1]))')),degree=2,F=Force,domain=mesh)





#Define auxiliry field for Stress intensity factor for K1
k1_aux1 = 1
#k2_aux1 = 0
u_kaux1 = Expression(["sqrt(sqrt(x[0]*x[0]+x[1]*x[1])/(2*pi))*(k1_aux1*((kappa-cos(atan2(x[1], x[0])))*cos(atan2(x[1], x[0])/2)/(2*mu)))",
                    "sqrt(sqrt(x[0]*x[0]+x[1]*x[1])/(2*pi))*(k1_aux1*((kappa-cos(atan2(x[1], x[0])))*sin(atan2(x[1], x[0])/2)/(2*mu)))"],
                    degree=2, mu=mu, kappa=kappav , k1_aux1=k1_aux1 , domain=mesh)


#Define auxiliry field for Stress intensity factor for K1
sigma_1 = Expression((('(1/sqrt(2*pi*sqrt(x[0]*x[0]+x[1]*x[1])))*(k1_aux1*(0.75*cos(atan2(x[1], x[0])/2)+0.25*cos(atan2(x[1], x[0])*5/2)))',
                       '(1/sqrt(2*pi*sqrt(x[0]*x[0]+x[1]*x[1])))*(k1_aux1*(-0.25*sin(atan2(x[1], x[0])/2)+0.25*sin(atan2(x[1], x[0])*5/2)))'),
                ('(1/sqrt(2*pi*sqrt(x[0]*x[0]+x[1]*x[1])))*(k1_aux1*(-0.25*sin(atan2(x[1], x[0])/2)+0.25*sin(atan2(x[1], x[0])*5/2)))',
                 '(1/sqrt(2*pi*sqrt(x[0]*x[0]+x[1]*x[1])))*(k1_aux1*(1.25*cos(atan2(x[1], x[0])/2)-0.25*cos(atan2(x[1], x[0])*5/2)))')),
                     degree=2,mu=mu, kappa=kappav,k1_aux1=k1_aux1 ,  domain=mesh)


#Define auxiliry field for Stress intensity factor for K2
#k1_aux2 = 0
k2_aux2 = 1
u_kaux2 = Expression(["sqrt(sqrt(x[0]*x[0]+x[1]*x[1])/(2*pi))*(k2_aux2*((2+kappa+cos(atan2(x[1], x[0])))*sin(atan2(x[1], x[0])/2)/(2*mu)))",
                    "sqrt(sqrt(x[0]*x[0]+x[1]*x[1])/(2*pi))*(k2_aux2*((2-kappa-cos(atan2(x[1], x[0])))*cos(atan2(x[1], x[0])/2)/(2*mu)))"],
                    degree=2, mu=mu, kappa=kappav, k2_aux2=k2_aux2, domain=mesh)

#Define auxiliry field for Stress intensity factor for K1
sigma_2 = Expression((('(1/sqrt(2*pi*sqrt(x[0]*x[0]+x[1]*x[1])))*(k2_aux2*(-1.75*sin(atan2(x[1], x[0])/2)-0.25*sin(atan2(x[1], x[0])*5/2)))',
                       '(1/sqrt(2*pi*sqrt(x[0]*x[0]+x[1]*x[1])))*(k2_aux2*(0.75*cos(atan2(x[1], x[0])/2)+0.25*cos(atan2(x[1], x[0])*5/2)))'),
                ('(1/sqrt(2*pi*sqrt(x[0]*x[0]+x[1]*x[1])))*(k2_aux2*(0.75*cos(atan2(x[1], x[0])/2)+0.25*cos(atan2(x[1], x[0])*5/2)))',
                 '(1/sqrt(2*pi*sqrt(x[0]*x[0]+x[1]*x[1])))*(k2_aux2*(-0.25*sin(atan2(x[1], x[0])/2)+0.25*sin(atan2(x[1], x[0])*5/2)))')),
                     degree=2,mu=mu, kappa=kappav, k2_aux2=k2_aux2, domain=mesh)


# In[14]:


solver_u.solve()
plt.figure(figsize=(12, 5))
plot(u, mode = 'displacement')


# In[19]:


I_value = ((0.5*inner(sigma_0(u),eps(u_aux))+0.5*inner(sigmax,eps(u)))*kdelta)-                   (dot(sigma_0(u),u_x(u_aux)) + dot(sigmax,u_x(u)))

I_k1 = ((0.5*inner(sigma_0(u),eps(u_kaux1))+0.5*inner(sigma_1,eps(u)))*kdelta)-                   (dot(sigma_0(u),u_x(u_kaux1)) + dot(sigma_1,u_x(u)))

I_k2 = ((0.5*inner(sigma_0(u),eps(u_kaux2))+0.5*inner(sigma_2,eps(u)))*kdelta)-                   (dot(sigma_0(u),u_x(u_kaux2)) + dot(sigma_2,u_x(u)))


#extract data for post-processing in paraview


#I for T-stress   
VI = VectorFunctionSpace(mesh, 'DG', 0)
I_ = Function(VI,name='Energy–momentum tensor')
I_.assign(project(I_value,VI))
file_I.write(I_)


#I for KI
VI1 = VectorFunctionSpace(mesh, 'DG', 0)
I_1 = Function(VI1,name='Energy–momentum tensor')
I_1.assign(project(I_k1,VI1))
file_Ik1.write(I_1)

#I for KII

VI2 = VectorFunctionSpace(mesh, 'DG', 0)
I_2 = Function(VI2,name='Energy–momentum tensor')
I_2.assign(project(I_k2,VI2))
file_Ik2.write(I_2)


# In[ ]:




