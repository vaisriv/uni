include("../../../code/sfd.jl")
using .SpaceFlightDynamics
using LinearAlgebra

r1 = [8000.0, 0.0, 0.0]
r2 = [7000.0, 7000.0, 0.0]
TOF = 3600.0

v1, v2, e, rp = solve_lambert(r1, r2, TOF; long_way=false)

r1_norm = norm(r1)
v_circ1 = [ 0.0,
            sqrt(μ_Earth / r1_norm),
            0.0 ]

r2_norm = norm(r2)

t_hat2 = [-r2[2], r2[1], 0.0] ./ r2_norm
v_circ2 = sqrt(μ_Earth / r2_norm) .* t_hat2

ΔV1 = norm(v1 .- v_circ1)
ΔV2 = norm(v2 .- v_circ2)
ΔV_total = ΔV1 + ΔV2

println("ΔV at departure (km/s): ", ΔV1)
println("ΔV at arrival   (km/s): ", ΔV2)
println("Total ΔV         (km/s): ", ΔV_total)
