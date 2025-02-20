#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Problem 2.15: Electric Field vs. r for a thick spherical shell
def plot_problem_2_15():
    # Parameters
    a = 1.0
    b = 2 * a
    epsilon_0 = 8.854e-12
    k = 1.0

    def E(r):
        if r < a:
            return 0
        elif r < b:
            return k * (r - a) / (epsilon_0 * r**2)
        else:
            return k * (b - a) / (epsilon_0 * r**2)

    rvals = np.linspace(0, 3 * a, 300)
    Eval = [E(r) for r in rvals]

    plt.figure()
    plt.plot(rvals, Eval)
    plt.xlabel("r")
    plt.ylabel("|E|")
    plt.title("Electric Field vs. r (Problem 2.15)")
    plt.show()


# Problem 2.17: Electric Field vs. y for an infinite plane slab of thickness 2d
def plot_problem_2_17():
    d = 1.0
    rho = 1.0
    epsilon_0 = 8.854e-12

    def E(y):
        if abs(y) <= d:
            return rho * y / epsilon_0
        else:
            return rho * d / epsilon_0 * np.sign(y)

    yvals = np.linspace(-2 * d, 2 * d, 400)
    Eval = [E(y) for y in yvals]

    plt.figure()
    plt.plot(yvals, Eval)
    plt.xlabel("y")
    plt.ylabel("E(y)")
    plt.title("Electric Field vs. y (Problem 2.17)")
    plt.show()


# Problem 2.21: Potential V(r) for a uniformly charged solid sphere
def plot_problem_2_21():
    R = 1.0
    q = 1.0
    epsilon_0 = 8.854e-12

    def V(r):
        if r >= R:
            return q / (4 * np.pi * epsilon_0) * (1 / r)
        else:
            return q / (4 * np.pi * epsilon_0) * ((3 * R**2 - r**2) / (2 * R**3))

    rvals = np.linspace(0.01, 2 * R, 400)
    Vvals = [V(r) for r in rvals]

    plt.figure()
    plt.plot(rvals, Vvals)
    plt.xlabel("r")
    plt.ylabel("V(r)")
    plt.title("Potential V(r) (Problem 2.21)")
    plt.show()


if __name__ == "__main__":
    # Uncomment the desired plot functions or run them sequentially.
    plot_problem_2_15()
    plot_problem_2_17()
    plot_problem_2_21()

