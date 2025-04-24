function two_body!(du, u, μ, t)
	# u = [ x, y, z, vx, vy, vz ]
	# du[1:3] = v
	# du[4:6] = acceleration
	@views du[1:3] .= u[4:6]
	r = @view u[1:3]
	r_norm = norm(r)
	@views du[4:6] .= -μ .* r ./ (r_norm^3)
end

function solve_2BP(initial::StateVectors,
		   tspan::Tuple{Float64, Float64};
		   μ::Float64 = μ_Earth,
		   reltol::Float64 = 1e-9,
		   abstol::Float64 = 1e-9,
		   int_pts::Int64 = 2)

	# Pack initial conditions into a 6‐vector
	u0 = vcat(initial.r, initial.v)

	# Set up and solve the ODE problem
	prob = ODEProblem(two_body!, u0, tspan, μ)
	sol  = solve(prob, Tsit5(), reltol=reltol, abstol=abstol, saveat=range(start=tspan[1], stop=tspan[2], length=int_pts))

	return [StateVectors(u[1:3], u[4:6]) for u in sol.u]
end

export solve_2BP
