%% +SpaceFlightDynamics/kepler.m
function E = kepler(M, e, tol, max_iter)
	if nargin < 4
		max_iter = 1000;
	end
	if nargin < 3
		tol = 1e-6;
	end
	M = mod(M, 2*pi);
	if M > pi
		M = M - 2*pi;
	end
	E = M;
	for iter = 1:max_iter
		f = E - e*sin(E) - M;
		fp = 1 - e*cos(E);
		E_new = E - f/fp;
		if abs(E_new - E) < tol
			E = E_new;
			return;
		end
		E = E_new;
	end
	error('Kepler''s equation did not converge after %d iterations', max_iter);
end
