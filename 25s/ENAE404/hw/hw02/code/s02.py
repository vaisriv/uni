import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

mu_sun = 1.32712440018e11


def state_to_keplerian(r_vec, v_vec, mu):
    """
    Convert Cartesian state vectors to orbital elements.

    Parameters:
      r_vec: Position vector (km)
      v_vec: Velocity vector (km/s)
      mu:    Gravitational parameter (km^3/s^2)

    Returns:
      a         : semimajor axis (km)
      e         : eccentricity (unitless)
      inc       : inclination (rad)
      RAAN      : right ascension of the ascending node (rad)
      arg_peri  : argument of perigee (rad)
      nu        : true anomaly (rad)
    """
    r = np.array(r_vec)
    v = np.array(v_vec)
    r_norm = np.linalg.norm(r)
    v_norm = np.linalg.norm(v)

    # Specific angular momentum vector and magnitude
    h = np.cross(r, v)
    h_norm = np.linalg.norm(h)

    # Inclination
    inc = np.arccos(h[2] / h_norm)

    # Node vector (pointing toward ascending node)
    K = np.array([0, 0, 1])
    n = np.cross(K, h)
    n_norm = np.linalg.norm(n)

    # Eccentricity vector and eccentricity magnitude
    e_vec = (np.cross(v, h) / mu) - (r / r_norm)
    e = np.linalg.norm(e_vec)

    # Semimajor axis (using vis-viva equation)
    a = 1 / (2 / r_norm - v_norm**2 / mu)

    # RAAN
    if n_norm > 1e-8:
        RAAN = np.arccos(n[0] / n_norm)
        if n[1] < 0:
            RAAN = 2 * np.pi - RAAN
    else:
        RAAN = 0

    # Argument of perigee
    if n_norm > 1e-8 and e > 1e-8:
        arg_peri = np.arccos(np.dot(n, e_vec) / (n_norm * e))
        if e_vec[2] < 0:
            arg_peri = 2 * np.pi - arg_peri
    else:
        arg_peri = 0

    # True anomaly
    if e > 1e-8:
        nu = np.arccos(np.dot(e_vec, r) / (e * r_norm))
        if np.dot(r, v) < 0:
            nu = 2 * np.pi - nu
    else:
        # For nearly circular orbits, use angle from node vector
        if n_norm > 1e-8:
            nu = np.arccos(np.dot(n, r) / (n_norm * r_norm))
            if r[2] < 0:
                nu = 2 * np.pi - nu
        else:
            nu = 0

    return a, e, inc, RAAN, arg_peri, nu


def two_body_equations(t, state, mu):
    """
    Two-body equations for a central gravitational force.
    state: [rx, ry, rz, vx, vy, vz]
    """
    r = state[0:3]
    v = state[3:6]
    r_norm = np.linalg.norm(r)
    a = -mu * r / r_norm**3
    return np.concatenate((v, a))


if __name__ == "__main__":
    # Initial state for Didymos
    r0 = np.array([-2.39573e8, -2.35661e8, 9.54384e6])  # position in km
    v0 = np.array([12.4732, -9.74427, -0.87661])  # velocity in km/s
    state0 = np.concatenate((r0, v0))

    # Propagation time (seconds)
    tmaxDidymos = 7.0e7
    t_span = (0, tmaxDidymos)
    # Use 1000 time points
    t_eval = np.linspace(0, tmaxDidymos, 1000)

    # Propagate the orbit using ODE solver
    sol = sp.integrate.solve_ivp(
        fun=lambda t, y: two_body_equations(t, y, mu_sun),
        t_span=t_span,
        y0=state0,
        t_eval=t_eval,
        rtol=1e-9,
        atol=1e-9,
    )

    # Extract the propagated state vectors
    r_sol = sol.y[0:3, :].T  # positions (km)
    v_sol = sol.y[3:6, :].T  # velocities (km/s)

    # Initialize lists for each orbital element
    a_vals = []
    e_vals = []
    inc_vals = []  # in degrees
    RAAN_vals = []  # in degrees
    argp_vals = []  # in degrees
    nu_vals = []  # in degrees

    for r, v in zip(r_sol, v_sol):
        a_i, e_i, inc_i, RAAN_i, argp_i, nu_i = state_to_keplerian(r, v, mu_sun)
        a_vals.append(a_i)
        e_vals.append(e_i)
        inc_vals.append(np.degrees(inc_i))
        RAAN_vals.append(np.degrees(RAAN_i))
        argp_vals.append(np.degrees(argp_i))
        nu_vals.append(np.degrees(nu_i))

    # 3D Orbit Plot
    fig1 = plt.figure(figsize=(10, 8))
    ax1 = fig1.add_subplot(111, projection="3d")
    ax1.plot(r_sol[:, 0], r_sol[:, 1], r_sol[:, 2], "b-", label="Orbit Path")
    ax1.scatter(
        r_sol[0, 0], r_sol[0, 1], r_sol[0, 2], color="green", s=100, label="Start"
    )
    ax1.set_xlabel("X (km)")
    ax1.set_ylabel("Y (km)")
    ax1.set_zlabel("Z (km)")
    ax1.set_title("3D Orbit of Didymos")
    # Set equal axes
    max_range = np.max(np.abs(r_sol))
    ax1.set_xlim([-max_range, max_range])
    ax1.set_ylim([-max_range, max_range])
    ax1.set_zlim([-max_range, max_range])
    ax1.legend()

    # Osculating Orbital Elements Subplots
    fig2, axs = plt.subplots(3, 2, figsize=(14, 12), sharex=True)

    # Semimajor axis
    axs[0, 0].plot(sol.t / 86400, a_vals, "b-")
    axs[0, 0].set_ylabel("a (km)")
    axs[0, 0].set_title("Semimajor Axis")
    axs[0, 0].set_ylim([-max_range, max_range])
    axs[0, 0].grid(True)

    # Eccentricity
    axs[0, 1].plot(sol.t / 86400, e_vals, "r-")
    axs[0, 1].set_ylabel("e")
    axs[0, 1].set_title("Eccentricity")
    axs[0, 1].set_ylim([-max_range, max_range])
    axs[0, 1].grid(True)

    # Inclination
    axs[1, 0].plot(sol.t / 86400, inc_vals, "g-")
    axs[1, 0].set_ylabel("i (deg)")
    axs[1, 0].set_title("Inclination")
    axs[1, 0].set_ylim([-max_range, max_range])
    axs[1, 0].grid(True)

    # RAAN
    axs[1, 1].plot(sol.t / 86400, RAAN_vals, "m-")
    axs[1, 1].set_ylabel("RAAN (deg)")
    axs[1, 1].set_title("RAAN")
    axs[1, 1].set_ylim([-max_range, max_range])
    axs[1, 1].grid(True)

    # Argument of Perigee
    axs[2, 0].plot(sol.t / 86400, argp_vals, "c-")
    axs[2, 0].set_ylabel("omega (deg)")
    axs[2, 0].set_title("Argument of Perigee")
    axs[2, 0].set_xlabel("Time (days)")
    axs[2, 0].set_ylim([-max_range, max_range])
    axs[2, 0].grid(True)

    # True Anomaly
    axs[2, 1].plot(sol.t / 86400, nu_vals, "k-")
    axs[2, 1].set_ylabel("nu (deg)")
    axs[2, 1].set_title("True Anomaly")
    axs[2, 1].set_xlabel("Time (days)")
    axs[2, 1].set_ylim([-max_range, max_range])
    axs[2, 1].grid(True)

    plt.tight_layout()
    plt.show()
