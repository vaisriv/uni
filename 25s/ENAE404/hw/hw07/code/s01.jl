include("../../../code/sfd.jl")
using .SpaceFlightDynamics

r1 = [8000.0, 0.0, 0.0]

v1 = []
t_esc = 3600.0

sv = solve_2BP(StateVectors(r1, v1), (0.0, t_esc), μ=μ_Earth, T_spec=1e-4, int_pts = 500)

println("  sv = ", sv)
