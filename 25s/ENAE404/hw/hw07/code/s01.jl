# enae404 hw07
include("../../../code/sfd.jl")
using .SpaceFlightDynamics
using LinearAlgebra
using Plots
using LaTeXStrings

# problem 01
# givens
Tₛ = 1e-4
rₒ = 8000.0
r₁ = rₒ * [1.0, 0.0, 0.0]

# part a
vₒ = sqrt(μ_Earth / rₒ)
v₁ = vₒ * [0.0, 1.0, 0.0]
@show v₁

# part b
aᵣ = -1 * μ_Earth / rₒ^2
aₜ = Tₛ
a = [aᵣ, aₜ]
@show a

# part c
tₑ = vₒ / aₜ * (1 - (20 * aₜ^2 * rₒ^2 / vₒ^9)^(1 / 8))
@show tₑ

# part d
sv = solve_2BP_thrust(StateVectors(r₁, v₁), (0.0, 2 * tₑ), μ=μ_Earth, T_spec=Tₛ, int_pts=500)
vₑ = sv[end].v
@show vₑ

xs = [sv.r[1] for sv in sv]
ys = [sv.r[2] for sv in sv]
plt = plot(
    xs, ys, label="2BP Integration",
    title="Thrust Escape Trajectory",
    xlabel=L"x ($km$)",
    ylabel=L"y ($km$)",
    aspect_ratio=:equal,
    grid=true)
display(plt)

# part e
time_step = 2 * tₑ / length(sv)
tₑ_num = 0
for i ∈ eachindex(sv)
    ε = 0.5 * norm(sv[i].v)^2 - μ_Earth / norm(sv[i].r)
    if ε > 0
        global tₑ_num = i * time_step
        break
    end
end
@show tₑ_num

# part f
analytic_tesc(aₜ) = vₒ / aₜ * (1 - (20 * aₜ^2 * rₒ^2 / vₒ^9)^(1 / 8))

function numeric_tesc(aₜ; int_pts=2000)
    t_e = analytic_tesc(aₜ)
    t_end = 10 * t_e
    sv = solve_2BP_thrust(
        StateVectors(r₁, v₁),
        (0.0, t_end),
        μ=μ_Earth,
        T_spec=aₜ,
        int_pts=int_pts
    )
    N = length(sv)
    ts = range(0, t_end, length=N)
    ε = [0.5 * norm(sv[i].v)^2 - μ_Earth / norm(sv[i].r) for i in 1:N]
    idx = findfirst(ε .>= 0)
    if idx === nothing
        return NaN
    elseif idx == 1
        return ts[1]
    else
        t1, t2 = ts[idx-1], ts[idx]
        e1, e2 = ε[idx-1], ε[idx]
        return t1 - e1 * (t2 - t1) / (e2 - e1)
    end
end

T_specs = range(1e-5, 1e-3, length=10)
t_anal = [analytic_tesc(T) for T in T_specs]
t_num = [numeric_tesc(T) for T in T_specs]

plot(
	T_specs, t_anal,
    label=L"Analytical $t_{esc}$",
    xlabel=L"Specific thrust ($\frac{kN}{kg}\to\frac{km}{s^2}$)",
    ylabel=L"Escape time $t_{esc}$ ($s$)",
    yscale=:log10,
    marker=:star5,
    legend=:topright,
    grid=true
)
plot!(
    T_specs, t_num,
    label=L"Numerical $t_{esc}$",
    marker=:circle
)