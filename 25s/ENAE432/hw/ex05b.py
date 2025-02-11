import numpy as np
import scipy as sc
import pprint as pp

pp.pprint("ex05")
pp.pprint("question 2")

b = 8.61

# Define the numerator and denominator of Y(s)
# Numerator: 6b(s + 3)
numerator = 6 * b * np.array([1, 3])
# Denominator: s(s^2 + 4s + b)
denom1 = np.array([1, 0])       # represents s
denom2 = np.array([1, 4, b])      # represents s^2 + 4s + b
denominator = np.convolve(denom1, denom2)  # Polynomial convolution

# Find the poles of the system (roots of the denominator)
poles = np.roots(denominator)

# Perform partial fraction expansion
# The function returns (residues, poles, direct_terms)
residues, poles_res, direct_terms = sc.signal.residue(numerator, denominator)

# Calculate the phase angle of the residue corresponding to the complex pole
complex_residue = residues[1]
phase_angle_residue = np.angle(complex_residue)  # phase angle in radians

phase_angle_oscillations = phase_angle_residue

# Ensure the phase angle is within the range [-pi, pi]
if phase_angle_oscillations < -np.pi:
    phase_angle_oscillations += 2 * np.pi
elif phase_angle_oscillations > np.pi:
    phase_angle_oscillations -= 2 * np.pi

pp.pprint("Final phase angle (in radians, within [-pi, pi]):")
pp.pprint(phase_angle_oscillations)
