# enae404 hw07
include("../../../code/SFD.jl/SFD.jl")
using .SpaceFlightDynamics
using LinearAlgebra
using Plots

# problem 01
# givens
Tₛ = 1e-4
rₒ = 8000.0
r₁ = rₒ * [1.0, 0.0, 0.0]

# part a
vₒ = sqrt(μ_Earth/rₒ)
v₁ = vₒ * [0.0, 1.0, 0.0]
@show v₁

# part b
aᵣ = -1*μ_Earth/rₒ^2
aₜ = Tₛ
a = [aᵣ, aₜ]
@show a

# part c
tₑ = vₒ/aₜ*(1-(20*aₜ^2*rₒ^2/vₒ^9)^(1/8))
@show tₑ

# part d
sv = solve_2BP_thrust(StateVectors(r₁, v₁), (0.0, 2*tₑ), μ=μ_Earth, T_spec=Tₛ, int_pts=500)
vₑ = sv[end].v
@show vₑ

xs = [sv.r[1] for sv in sv]
ys = [sv.r[2] for sv in sv]
plt = plot(
	xs, ys, label = "2BP Integration",
	title = "Thrust Escape Trajectory",
	xlabel = "x (km)",
	ylabel = "y (km)",
	aspect_ratio = :equal,
	grid = true)
display(plt)

# part e
time_step = 2*tₑ/length(sv)
rₑ = rₒ*vₒ/((20*aₜ^2*rₒ^2)^(1/4))
@show time_step
@show rₑ
tₑ_num = 0
for i ∈ 1:length(sv)
	if norm(sv[i].r) >= rₑ
		@show norm(sv[i].r)
		@show i
		global tₑ_num = i*time_step
		break
	end
end
@show tₑ_num
