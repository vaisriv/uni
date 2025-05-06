function kepler!(M::Float64, e::Float64; tol::Float64 = 1e-6, max_iter::Int = 1000)
	# normalize M to [-pi, pi]
	M = mod(M, 2*pi)
	if M > pi
		M -= 2*pi
	end

	# initial guess for E
	E = M
	for iter in 1:max_iter
		f = E - e*sin(E) - M
		fp = 1 - e*cos(E)
		E_new = E - f/fp
		if abs(E_new - E) < tol
			return E_new
		end
		E = E_new
	end
	error("Kepler's equation did not converge after $max_iter iterations")
end

function update_orbital_elements(oe::OrbitalElements, dt::Float64; μ::Float64 = μ_Earth)
	e = oe.e
	ν0 = deg2rad(oe.ν_deg)

	# initial eccentric anomaly E₀ from the true anomaly
	# tan(ν/2) = sqrt((1+e)/(1-e)) * tan(E/2)
	E0 = 2 * atan( sqrt((1 - e)/(1 + e)) * tan(ν0/2) )

	# mean anomaly at epoch
	M0 = E0 - e*sin(E0)

	# compute the mean motion n (rad/s)
	n = sqrt(μ / oe.a^3)

	# new mean anomaly after time dt
	M = M0 + n*dt

	# new eccentric anomaly E
	E = kepler!(M, e)

	# new true anomaly from E
	# ν = 2 * atan( sqrt((1+e)/(1-e)) * tan(E/2) )
	ν = 2 * atan( sqrt((1 + e)/(1 - e)) * tan(E/2) )
	ν = mod(ν, 2*pi)  # ensure ν is in the range [0, 2π)

	# new OrbitalElements with updated ν
	return OrbitalElements(oe.a, oe.e, oe.i_deg, oe.Ω_deg, oe.ω_deg, rad2deg(ν))
end

function solve_kepler(oe::OrbitalElements, dt::Float64; μ::Float64 = μ_Earth)
	oe_new = update_orbital_elements(oe, dt, μ=μ)
	sv_new = oe_to_sv(oe_new, μ=μ)
	return sv_new, oe_new
end

export solve_kepler
