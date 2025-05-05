%% +SpaceFlightDynamics/solve_kepler.m
function [sv_new, oe_new] = solve_kepler(oe, dt, mu)
	if nargin < 3
		mu = muEarth();
	end
	oe_new = update_orbital_elements(oe, dt, mu);
	sv_new = oe_to_sv(oe_new, mu);
end
