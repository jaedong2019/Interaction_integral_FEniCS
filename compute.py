import numpy as np


path = "../CN_AT1_E3000_beta30/"

file = "k1"

file2 = "k2"

file3 = "T-stress"

data1 = np.loadtxt(path + file + '/contour1.txt', delimiter=',', skiprows=1)
data2 = np.loadtxt(path + file + '/contour2.txt', delimiter=',', skiprows=1)
data3 = np.loadtxt(path + file + '/contour3.txt', delimiter=',', skiprows=1)
data4 = np.loadtxt(path + file + '/contour4.txt', delimiter=',', skiprows=1)
data5 = np.loadtxt(path + file + '/contour5.txt', delimiter=',', skiprows=1)


# Compute value of J_integral

I_value_k1 = -1*data1[1] + data2[2] + data3[1] + -1*data4[2] + -1*data5[1]
E = 1
print('K1_value = ' + str(I_value_k1*E/2))


data6 = np.loadtxt(path + file2 + '/contour1.txt', delimiter=',', skiprows=1)
data7 = np.loadtxt(path + file2 + '/contour2.txt', delimiter=',', skiprows=1)
data8 = np.loadtxt(path + file2 + '/contour3.txt', delimiter=',', skiprows=1)
data9 = np.loadtxt(path + file2 + '/contour4.txt', delimiter=',', skiprows=1)
data10 = np.loadtxt(path + file2 + '/contour5.txt', delimiter=',', skiprows=1)


I_value_k2 = -1*data6[1] + data7[2] + data8[1] + -1*data9[2] + -1*data10[1]

print('K2_value = ' + str(I_value_k2*E/2))

print('K ratio = ' + str(I_value_k2/I_value_k1))


data11 = np.loadtxt(path + file3 + '/contour1.txt', delimiter=',', skiprows=1)
data12 = np.loadtxt(path + file3 + '/contour2.txt', delimiter=',', skiprows=1)
data13 = np.loadtxt(path + file3 + '/contour3.txt', delimiter=',', skiprows=1)
data14 = np.loadtxt(path + file3 + '/contour4.txt', delimiter=',', skiprows=1)
data15 = np.loadtxt(path + file3 + '/contour5.txt', delimiter=',', skiprows=1)


I_value_T = -1*data11[1] + data12[2] + data13[1] + -1*data14[2] + -1*data15[1]

print('T-stress = ' + str(I_value_T*E/1))

