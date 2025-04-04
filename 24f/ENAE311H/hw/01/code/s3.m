syms x y
f1 = subs(int(x^2+2*y^2+50, y, [2 4]), x, 3)
f2 = subs(int(x^2+2*y^2+50, x, [3 5]), y, 2)
f3 = subs(int(x^2+2*y^2+50, x, [3 5]), y, 4)
f4 = subs(int(x^2+2*y^2+50, y, [2 4]), x, 5)
fx = f1+f4
fy = f2+f3
f = sqrt(fx^2+fy^2)
ang = rad2deg(atan(fy/fx))

m1 = subs(int((x^2+2*y^2+50)*x, y, [2 4]), x, 3)
m2 = subs(int((x^2+2*y^2+50)*y, x, [3 5]), y, 2)
m3 = subs(int((x^2+2*y^2+50)*y, x, [3 5]), y, 4)
m4 = subs(int((x^2+2*y^2+50)*x, y, [2 4]), x, 5)

m = m1-m2+m3-m4

cop_x = (m1 + m4) / (f1 + f4)
cop_y = (m2 + m3) / (f2 + f3)