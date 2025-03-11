a = 26562 * u.km        # semi-major axis
ecc = 0.3 * u.one       # eccentricity
inc = 40 * u.deg        # inclination
raan = 0 * u.deg        # right ascension of the ascending node
argp = 0 * u.deg        # argument of perigee
nu = 0 * u.deg          # true anomaly (set to 0 for the initial state)

Orbit_B = Orbit.from_classical(Earth, a, ecc, inc, raan, argp, nu)
Spacecraft_B = EarthSatellite(Orbit_B, None)
t_span = time_range(start=Orbit_B.epoch, end=Orbit_B.epoch + 24.0 * u.h, num_values=150)

gp = GroundtrackPlotter()
gp.update_layout(title="Spacecraft B groundtrack")

gp.plot(
    Spacecraft_B,
    t_span,
    label="Spacecraft B",
    color="red",
    marker={
        "size": 10,
        "symbol": "triangle-right",
        "line": {"width": 1, "color": "black"},
    },
)

# gp.update_geos(projection_type="orthographic")
gp.fig.show()
