function solve_gibbs(
	r1::Vector{Float64},
	r2::Vector{Float64},
	r3::Vector{Float64};
	μ::Float64 = μ_Earth
)
	# cross‐products
	c12 = cross(r1, r2)
	c23 = cross(r2, r3)
	c31 = cross(r3, r1)

	# N and D vectors
	N = c12*norm(r3) + c23*norm(r1) + c31*norm(r2)
	D = c12 + c23 + c31

	# S vector
	S =  r1*(norm(r2)-norm(r3)) +
		r2*(norm(r3)-norm(r1)) +
		r3*(norm(r1)-norm(r2))

	# scalar prefactor
	factor = sqrt( μ / (norm(N)*norm(D)) )

	# Gibbs velocity at r2
	v2 = factor * ( cross(D, r2)/norm(r2) + S )

	return v2
end

export solve_gibbs
