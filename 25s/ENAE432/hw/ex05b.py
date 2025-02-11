import numpy as np
import sympy as sp
import pprint as pp

pp.pprint("ex05")
pp.pprint("question 2")

# Define the symbol and parameter
s = sp.symbols('s')
b_val = 8.61

# Define the Laplace transform Y(s)
Y = 6 * b_val * (s + 3) / (s * (s**2 + 4*s + b_val))

# Perform partial fraction expansion
Y_pf = sp.apart(Y)
print("Partial Fraction Expansion:")
sp.pprint(Y_pf)
# Expected output:
# 18/s + (-18*s - 20.34)/(s**2 + 4*s + 8.61)

# From the partial fractions, we write:
# (-18*s - 20.34) = -18*(s+2) + 15.66
# so that the oscillatory term is:
#   -18*(s+2)/( (s+2)**2 + 4.61 ) + 15.66/( (s+2)**2 + 4.61 )
#
# Its inverse Laplace transform is:
#   -18 * e^(-2t) * cos(omega*t) + (15.66/omega) * e^(-2t) * sin(omega*t)
#
# with omega = sqrt(b_val - 4) = sqrt(4.61)
omega = np.sqrt(b_val - 4)  # sqrt(4.61) ≈ 2.146

# The coefficients in the oscillatory part are:
amp_cos = -18
amp_sin_term = 15.66 / omega  # coefficient in front of sin(t*omega)

# When writing the oscillatory part as A*e^(-2t)*cos(omega*t + phi),
# we require that:
#   A*cos(phi) = amp_cos = -18
#   -A*sin(phi) = amp_sin_term   -->  A*sin(phi) = -amp_sin_term
#
# Thus, the phase phi is given by:
phi = np.arctan2(-amp_sin_term, amp_cos)
print("\nPhase angle (in radians):")
print(phi)
