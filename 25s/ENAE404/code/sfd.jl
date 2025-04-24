module SpaceFlightDynamics
	using LinearAlgebra
	using DifferentialEquations

	μ_Earth = 398600.4418 # km^3/s_2
	μ_Sun = 1.32712e11 # km^3/s_2
	R_Earth = 6378.1363 # km

	include("./oe_sv.jl")
	include("./2BP.jl")
	include("./kepler.jl")
	include("./lambert.jl")
	include("./gibbs.jl")

	export μ_Earth, μ_Sun, R_Earth
end
