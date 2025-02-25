import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Earth's gravitational parameter (km^3/s^2)
mu = 398600.0


def keplerian_to_cartesian(a, e, inc, RAAN, arg_perigee, nu, mu):
    """
    Convert orbital elements to Cartesian state vectors (position, velocity)
    Inputs:
      a         - semimajor axis (km)
      e         - eccentricity (unitless)
      inc       - inclination (rad)
      RAAN      - right ascension of the ascending node (rad)
      arg_perigee - argument of perigee (rad)
      nu        - true anomaly (rad)
      mu        - gravitational parameter (km^3/s^2)
    Returns:
      r_eci, v_eci: position (km) and velocity (km/s) vectors in the ECI frame.
    """
    # Compute the distance (km) from the central body
    r = a * (1 - e**2) / (1 + e * np.cos(nu))

    # Position in the perifocal (PQW) frame
    r_perifocal = np.array([r * np.cos(nu), r * np.sin(nu), 0.0])

    # Parameter p
    p = a * (1 - e**2)
    # Velocity in the perifocal frame
    v_perifocal = np.array(
        [-np.sqrt(mu / p) * np.sin(nu), np.sqrt(mu / p) * (e + np.cos(nu)), 0.0]
    )

    # Rotation matrix from perifocal to ECI frame
    cos_O = np.cos(RAAN)
    sin_O = np.sin(RAAN)
    cos_w = np.cos(arg_perigee)
    sin_w = np.sin(arg_perigee)
    cos_i = np.cos(inc)
    sin_i = np.sin(inc)

    # Transformation matrix (from PQW to ECI)
    R = np.array(
        [
            [
                cos_O * cos_w - sin_O * sin_w * cos_i,
                -cos_O * sin_w - sin_O * cos_w * cos_i,
                sin_O * sin_i,
            ],
            [
                sin_O * cos_w + cos_O * sin_w * cos_i,
                -sin_O * sin_w + cos_O * cos_w * cos_i,
                -cos_O * sin_i,
            ],
            [sin_w * sin_i, cos_w * sin_i, cos_i],
        ]
    )

    # Convert position and velocity into ECI frame
    r_eci = R @ r_perifocal
    v_eci = R @ v_perifocal

    return r_eci, v_eci


def two_body_equations(t, state, mu):
    """
    Equations of motion for the two-body problem.
    state: [rx, ry, rz, vx, vy, vz]
    """
    r = state[0:3]
    v = state[3:6]
    r_norm = np.linalg.norm(r)
    # Gravitational acceleration
    a = -mu * r / r_norm**3
    return np.concatenate((v, a))


def state_to_keplerian(r_vec, v_vec, mu):
    """
    Compute orbital elements from state vectors.
    Returns: a, e, inc, RAAN, arg_perigee, nu (all in SI units, angles in rad)
    """
    r = np.array(r_vec)
    v = np.array(v_vec)
    r_norm = np.linalg.norm(r)
    v_norm = np.linalg.norm(v)

    # Specific angular momentum vector and its magnitude
    h = np.cross(r, v)
    h_norm = np.linalg.norm(h)

    # Inclination
    inc = np.arccos(h[2] / h_norm)

    # Node vector (pointing towards ascending node)
    K = np.array([0, 0, 1])
    n = np.cross(K, h)
    n_norm = np.linalg.norm(n)

    # Eccentricity vector
    e_vec = (np.cross(v, h) / mu) - (r / r_norm)
    e = np.linalg.norm(e_vec)

    # Semimajor axis (using vis-viva)
    a = 1 / (2 / r_norm - v_norm**2 / mu)

    # Right ascension of the ascending node (RAAN)
    if n_norm != 0:
        RAAN = np.arccos(n[0] / n_norm)
        if n[1] < 0:
            RAAN = 2 * np.pi - RAAN
    else:
        RAAN = 0

    # Argument of perigee
    if n_norm != 0 and e > 1e-8:
        arg_perigee = np.arccos(np.dot(n, e_vec) / (n_norm * e))
        if e_vec[2] < 0:
            arg_perigee = 2 * np.pi - arg_perigee
    else:
        arg_perigee = 0

    # True anomaly
    if e > 1e-8:
        nu = np.arccos(np.dot(e_vec, r) / (e * r_norm))
        if np.dot(r, v) < 0:
            nu = 2 * np.pi - nu
    else:
        # For circular orbits, true anomaly is undefined; using angle from node vector
        if n_norm != 0:
            nu = np.arccos(np.dot(n, r) / (n_norm * r_norm))
            if r[2] < 0:
                nu = 2 * np.pi - nu
        else:
            nu = 0

    return a, e, inc, RAAN, arg_perigee, nu


if __name__ == "__main__":
    # Given orbital elements:
    # a in km, e unitless, angles in degrees (convert to radians)
    a = 2e4  # km
    e = 0.4
    inc = np.radians(100)  # inclination
    RAAN = np.radians(30)  # Right Ascension of Ascending Node
    arg_perigee = np.radians(15)  # Argument of perigee
    nu = np.radians(15)  # True anomaly

    # Convert orbital elements to Cartesian state (position and velocity)
    r0, v0 = keplerian_to_cartesian(a, e, inc, RAAN, arg_perigee, nu, mu)
    state0 = np.concatenate((r0, v0))

    # Compute the orbital period using Kepler's third law (T in seconds)
    T = 2 * np.pi * np.sqrt(a**3 / mu)
    print(f"Orbital period: {T/3600:.2f} hours")

    # Time span for propagation (one period)
    t_span = (0, T)
    # Evaluation times (using 1000 sample points)
    t_eval = np.linspace(0, T, 1000)

    # Propagate the orbit using ODE solver
    sol = sp.integrate.solve_ivp(
        fun=lambda t, y: two_body_equations(t, y, mu),
        t_span=t_span,
        y0=state0,
        t_eval=t_eval,
        rtol=1e-9,
        atol=1e-9,
    )

    # Extract position and velocity from the solution
    r_sol = sol.y[0:3, :].T  # shape (N, 3)
    v_sol = sol.y[3:6, :].T  # shape (N, 3)

    # Compute specific mechanical energy at each time step: E = v^2/2 - mu/|r|
    energy = np.array(
        [
            0.5 * np.linalg.norm(v) ** 2 - mu / np.linalg.norm(r)
            for r, v in zip(r_sol, v_sol)
        ]
    )
    E0 = energy[0]
    energy_deviation = energy - E0

    # Osculating Orbital Elements vs Time
    a_vals = []
    e_vals = []
    inc_vals = []
    RAAN_vals = []
    arg_perigee_vals = []
    nu_vals = []
    for r, v in zip(r_sol, v_sol):
        a_i, e_i, inc_i, RAAN_i, argp_i, nu_i = state_to_keplerian(r, v, mu)
        a_vals.append(a_i)
        e_vals.append(e_i)
        inc_vals.append(np.degrees(inc_i))  # converting to degrees for plotting
        RAAN_vals.append(np.degrees(RAAN_i))
        arg_perigee_vals.append(np.degrees(argp_i))
        nu_vals.append(np.degrees(nu_i))

    # Plotting
    fig = plt.figure(figsize=(14, 10))

    # 3D Orbit plot with equal axes
    ax1 = fig.add_subplot(221, projection="3d")
    ax1.plot(r_sol[:, 0], r_sol[:, 1], r_sol[:, 2], "b-", label="Orbit")
    ax1.scatter(
        r_sol[0, 0],
        r_sol[0, 1],
        r_sol[0, 2],
        color="green",
        marker="o",
        s=100,
        label="Start",
    )
    ax1.set_title("3D Orbit")
    ax1.set_xlabel("X (km)")
    ax1.set_ylabel("Y (km)")
    ax1.set_zlabel("Z (km)")
    # Set equal aspect ratio
    max_range = np.max(np.abs(r_sol))
    ax1.set_xlim([-max_range, max_range])
    ax1.set_ylim([-max_range, max_range])
    ax1.set_zlim([-max_range, max_range])
    ax1.legend()

    # Energy deviation plot
    ax2 = fig.add_subplot(222)
    ax2.plot(sol.t / 3600, energy_deviation, "r-")
    ax2.set_xlabel("Time (hours)")
    ax2.set_ylabel("Energy deviation (km^2/s^2)")
    ax2.set_title("Deviation in Energy vs Time")
    ax2.set_ylim([-max_range, max_range])
    ax2.grid(True)

    # Osculating orbital elements plot (a, e, i, RAAN, arg_perigee, nu)
    ax3 = fig.add_subplot(212)
    # ax3.plot(sol.t / 3600, a_vals, label='a (km)') # skip plotting a, as it is orders of magnitude outside range of others
    ax3.plot(sol.t / 3600, e_vals, label="e")
    ax3.plot(sol.t / 3600, inc_vals, label="i (deg)")
    ax3.plot(sol.t / 3600, RAAN_vals, label="RAAN (deg)")
    ax3.plot(sol.t / 3600, arg_perigee_vals, label="omega (deg)")
    ax3.plot(sol.t / 3600, nu_vals, label="nu (deg)")
    ax3.set_xlabel("Time (hours)")
    ax3.set_title("Osculating Orbital Elements vs Time")
    ax3.legend()
    ax3.grid(True)

    plt.tight_layout()
    plt.show()
