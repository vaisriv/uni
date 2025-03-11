a = 42164 * u.km        # semi-major axis
ecc = 0.3 * u.one       # eccentricity
inc = 30 * u.deg        # inclination
raan = 0 * u.deg        # right ascension of the ascending node
argp = 70 * u.deg        # argument of perigee
nu = 0 * u.deg          # true anomaly (set to 0 for the initial state)

Orbit_D = Orbit.from_classical(Earth, a, ecc, inc, raan, argp, nu)
Spacecraft_D = EarthSatellite(Orbit_D, None)
t_span = time_range(start=Orbit_D.epoch, end=Orbit_D.epoch + 24.0 * u.h, num_values=150)

gp = GroundtrackPlotter()
gp.update_layout(title="Spacecraft D groundtrack")

gp.plot(
    Spacecraft_D,
    t_span,
    label="Spacecraft D",
    color="red",
    marker={
        "size": 10,
        "symbol": "triangle-right",
        "line": {"width": 1, "color": "black"},
    },
)

# gp.update_geos(projection_type="orthographic")
gp.fig.show()
