include("../../../code/sfd.jl")
using .SpaceFlightDynamics

r1 = [-6_979.49190,   208.846535,  -573.801140]
r2 = [-6_966.33930,   267.474976,  -734.881458]
r3 = [-6_949.96267,   325.979638,  -895.621695]

v2 = solve_gibbs(r1, r2, r3)
println("Estimated velocity at t₂ (km/s): ", v2)
