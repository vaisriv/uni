struct OrbitalElements
	a::Float64
	e::Float64
	i_deg::Float64
	Ω_deg::Float64
	ω_deg::Float64
	ν_deg::Float64
end

struct StateVectors
	r::Vector{Float64}
	v::Vector{Float64}
end

function oe_to_sv(oe::OrbitalElements; μ::Float64 = μ_Earth)
	# unpack orbital elements
	a     = oe.a
	e     = oe.e
	i_deg = oe.i_deg
	Ω_deg = oe.Ω_deg
	ω_deg = oe.ω_deg
	ν_deg = oe.ν_deg

	# convert OEs from degrees to radians
	i = deg2rad(i_deg)
	Ω = deg2rad(Ω_deg)
	ω = deg2rad(ω_deg)
	ν = deg2rad(ν_deg)

	# compute radius
	r_mag = a * (1 - e^2) / (1 + e*cos(ν))

	# perifocal position
	r_pf = [
		r_mag*cos(ν);
		r_mag*sin(ν);
		0.0
	]

	# semi-latus rectum
	p = a * (1 - e^2)

	# perifocal velocity
	v_pf = [
		-sqrt(μ/p)*sin(ν);
		sqrt(μ/p)*(e + cos(ν));
		0.0
	]

	# rotate from perifocal frame to geocentric equatorial frame
	R = [
		cos(Ω)*cos(ω) - sin(Ω)*sin(ω)*cos(i)  -cos(Ω)*sin(ω) - sin(Ω)*cos(ω)*cos(i)   sin(Ω)*sin(i);
		sin(Ω)*cos(ω) + cos(Ω)*sin(ω)*cos(i)  -sin(Ω)*sin(ω) + cos(Ω)*cos(ω)*cos(i)  -cos(Ω)*sin(i);
		sin(ω)*sin(i)                          cos(ω)*sin(i)                          cos(i)
	]

	# rotate to inertial frame
	r = R * r_pf
	v = R * v_pf

	return StateVectors(r, v)
end

export OrbitalElements, StateVectors, oe_to_sv
