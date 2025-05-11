include("../../../code/SFD.jl/SFD.jl")
using .SpaceFlightDynamics

# Case 1: short‐way
r1_c1 = [8000.0, 0.0, 0.0]
r2_c1 = [7000.0, 7000.0, 0.0]
TOF_c1 = 3600.0

v1_c1, v2_c1, e_c1, rp_c1 = solve_lambert(r1_c1, r2_c1, TOF_c1; long_way=false)

println("Case 1 (short way):")
println("  v₁ = ", v1_c1)
println("  v₂ = ", v2_c1)
println("  e  = ", e_c1)
println("  rₚ = ", rp_c1, " km\n")

# Case 2: long‐way, using Earth radius
r1_c2 = [0.5, 0.6, 0.7] .* R_Earth
r2_c2 = [0.0, -1.0, 0.0] .* R_Earth
TOF_c2 = 16135.0

v1_c2, v2_c2, e_c2, rp_c2 = solve_lambert(r1_c2, r2_c2, TOF_c2; long_way=true)

println("Case 2 (long way):")
println("  v₁ = ", v1_c2)
println("  v₂ = ", v2_c2)
println("  e  = ", e_c2)
println("  rₚ = ", rp_c2, " km")
