# Homework Assignment 7: Thrust Calculations and Porkchop Plot 

ENAE404: Space Flight Dynamics

Submit your assignment on Gradescope. For problems requiring coding, attach your code.

1. Modify your 2BP numerical integrator to include a thrust force in the direction of the velocity (specific thrust of $1 \times 10^{-4} \mathrm{kN} / \mathrm{kg}$ ). Consider a spacecraft orbiting Earth with an initial position of $[8000,0,0]$ $(\mathrm{km})$ in an equatorial, circular orbit (velocity in $\hat{y}$ direction).
(a) (2pts) Give the initial velocity vector of the spacecraft.
(b) (4pts) Write an expression for the specific forces (i.e. accelerations) acting on the spacecraft in terms of $\hat{r}$ and $\hat{v}$.
(c) (2pts) Using the analytical relations described in class, calculate the time of flight predicted to be required to reach escape velocity $\left(t_{e s c}\right)$.
(d) (10pts) Propagate the trajectory using your numerical integrator for $2 t_{\text {esc }}$. Plot the 2 D trajectory (use 'grid on' and 'axis equal' commands) and give the velocity vector at the final epoch.
(e) (10pts) Using the output from your integrator, calculate the time required to escape. Note that the accuracy of your numerical estimate for $t_{e s c}$ should be within $\pm 20$ seconds. Compare the numerical and analytical values of $t_{\text {esc }}$ and discuss why the analytical solution over- or underestimates $t_{\text {esc }}$.
(f) (10pts) Repeat your numerical integration for at least 10 evenly spaced magnitudes of specific thrust ranging from $\left(1 \times 10^{-5} \mathrm{kN} / \mathrm{kg}\right.$ to $\left.1 \times 10^{-3} \mathrm{kN} / \mathrm{kg}\right)$ AND increasing your propagation time to $10 t_{e s c}$. Plot the analytical prediction of the time required to escape ( $t_{e s c}$ ) and the numerically integrated $t_{\text {esc }}$ as a function of specific thrust. Use a log scale on the y axis ( 'set(gca,'yscale', 'log')').
(g) (3pts) Using evidence from your plot in part 1f, discuss the limitations of the analytical solution for $t_{e s c}$.
2. (10 points) Consider a Mars-observing satellite with a periapsis altitude of 1000 km and an eccentricity of 0.25 .

- Calculate the mass of the propellants used to circularize the spacecraft's orbit at periapsis (initial spacecraft mass is 1500 kg ), assuming a specific impulse of 250 sec .
- Given a structural ratio of 0.15 and assuming all of the rocket's fuel is used in this maneuver, calculate the payload fraction of the spacecraft.

3. (30pts) You are designing a robotic mission to Mars. Your goal is to identify the best launch date and Earth-Mars transfer duration for your robotic mission to Mars. First, create a wrapper script to feed the positions of Mars and Earth into your Lambert's solver function. Use the provided findEarth.m, findMars.m, findE.m, and ymdhms2jd.m functions. Note that you must modify findEarth and findMars so that they call your code to convert orbital elements into Cartesian position and velocity vectors. Create a porkchop plot (make a contour plot in Matlab, see example online) showing the time of flight, the C3 ( $V_{i n f}^{2}$ at Earth) and $V_{i n f}$ at Mars as a function of the arrival and departure dates. Consider departure dates starting at noon on August 1, 2022 and arrival dates starting at January 28, 2023 (180 days later). Consider transfer durations between 45 and 500 days. Label your contours usefully.
