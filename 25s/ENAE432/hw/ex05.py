from scipy.integrate import solve_ivp
import numpy as np
import pprint as pp

pp.pprint("ex05")
pp.pprint("question 1")

def ydef(t, y, a, b):
    dydt = y[2]+5*y[1]+6*y[0]+15*b*np.exp(-b*t)-15*a*np.exp(-b*t)

    3*u[1]+3*a*u[0]

solve_ivp(ydef)
