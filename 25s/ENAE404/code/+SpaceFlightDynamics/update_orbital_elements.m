%% +SpaceFlightDynamics/update_orbital_elements.m
function oe_new = update_orbital_elements(oe, dt, mu)
	if nargin < 3
		mu = SpaceFlightDynamics.muEarth();
	end
	e = oe.e;
	nu0 = deg2rad(oe.nu_deg);
	E0 = 2*atan( sqrt((1 - e)/(1 + e)) * tan(nu0/2) );
	M0 = E0 - e*sin(E0);
	n = sqrt(mu/oe.a^3);
	M = M0 + n*dt;
	E = SpaceFlightDynamics.kepler(M, e);
	nu = 2*atan( sqrt((1 + e)/(1 - e)) * tan(E/2) );
	nu = mod(nu, 2*pi);
	oe_new = SpaceFlightDynamics.OrbitalElements(oe.a, oe.e, oe.i_deg, oe.Omega_deg, oe.omega_deg, rad2deg(nu));
end
