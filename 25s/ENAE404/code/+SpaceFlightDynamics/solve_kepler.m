%% +SpaceFlightDynamics/solve_kepler.m
function [sv_new, oe_new] = solve_kepler(oe, dt, mu)
	if nargin < 3
		mu = SpaceFlightDynamics.muEarth();
	end
	oe_new = SpaceFlightDynamics.update_orbital_elements(oe, dt, mu);
	sv_new = SpaceFlightDynamics.oe_to_sv(oe_new, mu);
end
