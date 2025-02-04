# vec_r_dd + mu/r^3*vec_r = vec_0

using DifferentialEquations

function earthODE(dy, y, p, t)
	dy[1] = p[1]*y[1] - p[2]*y[2]
	dy[2] = p[2]*y[1] - p[3]*y[2]
end

y0 = [1.0, 0.0]
p = [1.0, 2.0, 3.0]
tspan = (0.0, 10.0)

prob = ODEProblem(earthODE, y0, tspan, p)
sol = solve(prob)
