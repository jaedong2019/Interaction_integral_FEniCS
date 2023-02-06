// Gmsh project created on Tue Jul  6 18:58:14 2021
SetFactory("OpenCASCADE");

ad = 25.4;
f0 = 0.2/ad;
f1 = f0;

L = 457/ad;
W = 228/ad;
eta = 0.001;
a = 25.4/ad;

beta = 90;
theta = (90-beta)*Pi/180;
beta0 = beta*Pi/180;
c = Cos(theta);
s = Sin(theta);

 
//
Point(1) = {-W-a*c, -L-a*s, 0, f0*12};
//+
Point(2) = {W-a*c, -L-a*s, 0, f0*12};
//+
Point(3) = {W-a*c, L-a*s, 0, f0*12};
//+
Point(4) ={-W-a*c, L-a*s, 0, f0*12};
//+
Point(5) ={-a*c, eta-a*s, 0, f1};
//+
Point(6) ={a*c-a*c, a*s-a*s, 0, f1};
//+
Point(7) ={-a*c,-eta-a*s, 0, f1};
//+
Point(8) ={-a*c-a*c, -a*s-a*s, 0, f1};



//+
Line(1) = {5, 6};
//+
Line(2) = {6, 7};
//+
Line(3) = {7, 8};
//+
Line(4) = {8, 5};
//+
Line(5) = {4, 1};
//+
Line(6) = {1, 2};
//+
Line(7) = {2, 3};
//+
Line(8) = {3, 4};
//+
Curve Loop(1) = {8, 5, 6, 7};
//+
Curve Loop(2) = {1, 2, 3, 4};
//+
Plane Surface(1) = {1, 2};
//+
Rotate {{0, 0, 1}, {0, 0, 0}, -theta} {
  Surface{1}; 
}
//+
Physical Surface("1") = {1};
//+
Physical Curve("2") = {1};
//+
Physical Curve("3") = {3};


