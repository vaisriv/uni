# Homework Assignment 8: Quaternions and Torque Free Motion 

ENAE404: Space Flight Dynamics

Submit on Gradescope. For problems solved in Matlab, attach your code.

1. (40 pts) The orientation of a spacecraft is given in terms of the 3-2-1 Euler Angles (i.e., yaw-pitch-roll) as $(30,40,10)$ degrees.
(a) ( 8 pts ) Give the rotation matrix from the inertial to the body-fixed frame.
(b) (12 pts) Calculate the principal rotation axis $\hat{e}$ and the principal rotation angle $\phi$.
(c) ( 8 pts ) Calculate the quarternions that describe this orientation of the spacecraft.
(d) (12 pts) Assume that ${ }^{B} \omega=(0.1,0.2,0)$ radians $/ \mathrm{sec}$ at the current time. What is the current quarternion rate of change (i.e., $\dot{\vec{\beta}}$ )?
2. ( 55 pts ) Write a code to numerically integrate the angular velocity vector for a torque-free rigid body with principal body-fixed axes. The body has the following body-fixed inertia matrix (units of $\mathrm{kg} \mathrm{m}^{2}$ ):

$$
[I]=\left[\begin{array}{ccc}
10 & 0 & 0 \\
0 & 20 & 0 \\
0 & 0 & 30
\end{array}\right]
$$

(a) (6 pts) Given $\omega=[10,0,30] \mathrm{deg} / \mathrm{sec}$ in the body-fixed frame, calculate the angular momentum magnitude and kinetic energy of the body.
(b) ( 6 pts plot +10 pts code) Given the above initial angular velocity, propagate the angular velocity for 100 seconds. On a single plot, plot the angular velocity components as a function of time.
(c) (10 pts) Plot the kinetic energy deviation and angular momentum magnitude deviation as a function of time. Discuss why you believe that your code is working.
(d) (11 pts) Create the polhode plot for this system. The angular momentum sphere should be a single color and the kinetic energy ellipsoid should be a single color. On top of the polhode, plot (as points) the time-varying body-fixed angular momentum. Use 'axis equal' and orient the plot so that you can see the angular momentum points.
(e) (7 pts) Given $\omega=[1,15,0] \mathrm{deg} / \mathrm{sec}$ in the body-fixed frame, propagate the angular velocity for 100 seconds. On a single plot, plot the angular velocity components as a function of time.
(f) (15 pts) Create the polhode plot for this system. The angular momentum sphere should be a single color and the kinetic energy ellipsoid should be a single color. On top of the polhode, plot (as points) the time-varying body-fixed angular momentum. Discuss why plots in e and f look significantly different from the plots in part b and d. Compare the energy between the system in part a and the current system.

