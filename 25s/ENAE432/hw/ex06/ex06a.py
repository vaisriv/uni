import sympy as sp
from sympy import pprint as print

print("ex06")
print("question 1")
print("----------")

# define variables and functions
# t, a, c, y(t), Y(s)
t, s, a, c = sp.symbols('t s a c', real=True)
y = sp.Function('y')(t)
Y = sp.Function('Y')(s)

# define ode
# G(s) = Y(s) / U(s) = 2 (s+a)² / (s² + 4 s + 3)
# U(s) = c*1(t)
G_s = (2*(s+a)**2)/(s**2+4*s+3)
U_s = c/s
Y_s = sp.simplify(G_s * U_s).subs({a: 2.46, c: 2.18})
print(sp.Eq(Y, Y_s))

# find y(t)
y_t = sp.inverse_laplace_transform(Y_s, s, t)
print(sp.Eq(y, sp.simplify(y_t)))

# find y(0)
y0_time = sp.limit(y_t, t, 0, dir='+')
print(sp.Eq(y.subs({t: 0}), sp.N(y0_time)))
