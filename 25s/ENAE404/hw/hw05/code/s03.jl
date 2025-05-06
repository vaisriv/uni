include("../../../code/SFD.jl/SFD.jl")
using .SpaceFlightDynamics

# sc: a (km) | e | i (deg) | Ω (deg) | ω (deg) | ν (deg)
# 1_oe: 15e3 | 0.4 | 60 | 45 | 0 | 145
# 2_oe: 21e3 | 0.6 | 90 | 0 | 0 | 35
oe_sc1 = OrbitalElements(15000.0, 0.4, 60.0, 45.0, 0.0, 145.0)
oe_sc2 = OrbitalElements(21000.0, 0.6, 90.0, 0.0, 0.0, 35.0)

# time step of 1 hr (in seconds)
dt = 3600.0

# new state vectors and oe for each spacecraft
sv_sc1_new, oe_sc1_new = predict_kepler(oe_sc1, dt)
sv_sc2_new, oe_sc2_new = predict_kepler(oe_sc2, dt)

println("Predicted State Vectors after $(dt) seconds:")
println("\nSpacecraft 1:")
println("\tPosition Vector (r): ", round.(sv_sc1_new.r, digits = 3), " km")
println("\tVelocity Vector (v): ", round.(sv_sc1_new.v, digits = 3), " km/s")
println("\nSpacecraft 2:")
println("\tPosition Vector (r): ", round.(sv_sc2_new.r, digits = 3), " km")
println("\tVelocity Vector (v): ", round.(sv_sc2_new.v, digits = 3), " km/s")

