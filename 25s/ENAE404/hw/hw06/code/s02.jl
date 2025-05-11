include("../../../code/SFD.jl/SFD.jl")
using .SpaceFlightDynamics
using Plots
plotlyjs()

# Case 1: short‐way
r1_c1 = [8000.0, 0.0, 0.0]
r2_c1 = [7000.0, 7000.0, 0.0]
TOF_c1 = 3600.0

v1_c1, v2_c1, e_c1, rp_c1 = solve_lambert(r1_c1, r2_c1, TOF_c1; long_way=false)
sv_c1 = solve_2BP(StateVectors(r1_c1, v1_c1), (0.0, TOF_c1), μ=μ_Earth, int_pts = 500)

r2_c1_diff = r2_c1 - sv_c1[end].r
v2_c1_diff = v2_c1 - sv_c1[end].v

println("Case 1 Final Position Vector Diff: ", r2_c1_diff)
println("Case 1 Final Velocity Vector Diff: ", v2_c1_diff)

# Case 2: long‐way, using Earth radius
r1_c2 = [0.5, 0.6, 0.7] .* R_Earth
r2_c2 = [0.0, -1.0, 0.0] .* R_Earth
TOF_c2 = 16135.0

v1_c2, v2_c2, e_c2, rp_c2 = solve_lambert(r1_c2, r2_c2, TOF_c2; long_way=true)
sv_c2 = solve_2BP(StateVectors(r1_c2, v1_c2), (0.0, TOF_c2), μ=μ_Earth, int_pts = 500)

r2_c2_diff = r2_c2 - sv_c2[end].r
v2_c2_diff = v2_c2 - sv_c2[end].v

println("Case 2 Final Position Vector Diff: ", r2_c2_diff)
println("Case 2 Final Velocity Vector Diff: ", v2_c2_diff)

xs = [sv.r[1] for sv in sv_c2]
ys = [sv.r[2] for sv in sv_c2]
zs = [sv.r[3] for sv in sv_c2]

θ = range(0,2π,length=60)
φ = range(0,π,length=30)
x_s = [R_Earth*sin(ϕ)*cos(θi) for ϕ in φ, θi in θ]
y_s = [R_Earth*sin(ϕ)*sin(θi) for ϕ in φ, θi in θ]
z_s = [R_Earth*cos(ϕ)          for ϕ in φ, θi in θ]

plt = plot(
    surface(x_s, y_s, z_s; opacity=1.0, legend=false),
    xlabel="x (km)", ylabel="y (km)", zlabel="z (km)",
    title="Case 2 Lambert Transfer (long way)",
)

plot!(plt, xs, ys, zs; lw=2, label="Transfer arc")
scatter!(plt, [r1_c2[1]], [r1_c2[2]], [r1_c2[3]]; markersize=2, markercolor=:green, label="Start")
scatter!(plt, [r2_c2[1]], [r2_c2[2]], [r2_c2[3]]; markersize=2, markercolor=:red,   label="End")

display(plt)
