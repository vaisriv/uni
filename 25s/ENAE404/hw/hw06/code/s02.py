from astropy import units as u
from poliastro.bodies import Earth
from poliastro.iod.izzo import lambert
from poliastro.twobody.orbit import Orbit
from poliastro.plotting import OrbitPlotter3D
import matplotlib.pyplot as plt

# 1) Define your known vectors
R_E = Earth.R.to(u.km)  # Earth radius in km

r1 = [0.5, 0.6, 0.7] * R_E
v1 = [-2.133759073847983,  7.024037548362913,  -2.9872627033871755] * u.km / u.s

# For completeness, also set r2 so we can scatter it later
r2 = [0.0, -1.0, 0.0] * R_E

TOF = 16135 * u.s  # time‐of‐flight

# 2) Solve the Lambert problem (long way)
#    lowpath=False picks the “long‐way” solution
v1_lambert, v2_lambert = lambert(
    Earth.k, r1, r2, TOF,
    lowpath=False
)

# 3) Build an Orbit from r1, v1_lambert
orbit = Orbit.from_vectors(Earth, r1, v1_lambert)

# 4) Plot in 3D with Earth
plotter = OrbitPlotter3D()
plotter.plot(orbit, label="Transfer arc")      # draws Earth + orbit
plotter.scatter(r1, color="green", label="Start")
plotter.scatter(r2, color="red",   label="End")

plt.title("Case 2 Lambert Transfer (long way)")
plt.show()
