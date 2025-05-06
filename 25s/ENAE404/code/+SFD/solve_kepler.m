function [sv_new, oe_new] = solve_kepler(oe, dt, mu)
%SOLVE_KEPLER Solve Kepler's problem 
% Solver for Kepler's problem
	if nargin < 3
		mu = SFD.mu_Earth();
	end
	oe_new = SFD.update_orbital_elements(oe, dt, mu);
	sv_new = SFD.oe2sv(oe_new, mu);
end
