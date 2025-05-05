%% +SpaceFlightDynamics/two_body.m
function du = two_body(t, u, mu)
	if nargin < 3
		mu = SpaceFlightDynamics.muEarth();
	end
	du = zeros(6,1);
	du(1:3) = u(4:6);
	r = u(1:3);
	r_norm = norm(r);
	du(4:6) = -mu*r/(r_norm^3);
end
