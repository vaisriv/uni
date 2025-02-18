import sympy as sp
from sympy import pprint as print

print("ex06")
print("question 2")
print("----------")

# define variables and functions
# t, a, b, y(t), u(t)
t, a, b = sp.symbols('t a b', real=True)
y = sp.Function('y')(t)
u = sp.Function('u')(t)

# setup laplace domain
delta = sp.DiracDelta(t)
s = sp.symbols('s', real=True, positive=True)
Y = sp.Function('Y')(s)

# define ode
# s² Y(s) + 3 a * s Y(s) = 3 b * s + 5
Y_s = (3*b*s+5)/(s*(s+3*a))
print(sp.Eq(Y, Y_s))

y_t = sp.inverse_laplace_transform(Y_s, s, t)
print(sp.Eq(y, y_t))

A_numeric = sp.simplify(5/(3*a)).subs(a, 1.07)
print(sp.Eq(sp.symbols('A'), A_numeric))
