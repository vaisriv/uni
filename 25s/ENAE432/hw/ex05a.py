import sympy as sp
import pprint as pp

pp.pprint("ex05")
pp.pprint("question 1")

t, a, b = sp.symbols('t a b', real=True)
y = sp.Function('y')(t)

# y''(t) + 5 y'(t) + 6 y(t) = 15*(a-b)*exp(-b*t)
ode = sp.Eq(y.diff(t, 2) + 5*y.diff(t) + 6*y, 15*(a - b)*sp.exp(-b*t))
ics = {
    y.subs(t, 0): 0,
    y.diff(t).subs(t, 0): 0
}

# Solve ODE: y(0)=0, y'(0)=0
solution = sp.dsolve(eq=ode, func=y, ics=ics)
numeric_solution = solution.subs({a: 3.71, b: 5.65})

pp.pprint("symbolic solution:")
sp.pprint(solution)

pp.pprint("numeric solution:")
sp.pprint(numeric_solution)
