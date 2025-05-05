%% +SpaceFlightDynamics/oe_to_sv.m
function sv = oe_to_sv(oe, mu)
	if nargin < 2
		mu = SpaceFlightDynamics.muEarth();
	end
	a = oe.a;
	e = oe.e;
	i = deg2rad(oe.i_deg);
	Omega = deg2rad(oe.Omega_deg);
	omega = deg2rad(oe.omega_deg);
	nu = deg2rad(oe.nu_deg);
	r_mag = a*(1 - e^2)/(1 + e*cos(nu));
	r_pf = [r_mag*cos(nu); r_mag*sin(nu); 0];
	p = a*(1 - e^2);
	v_pf = [-sqrt(mu/p)*sin(nu); sqrt(mu/p)*(e + cos(nu)); 0];
	Rmat = [cos(Omega)*cos(omega) - sin(Omega)*sin(omega)*cos(i), -cos(Omega)*sin(omega) - sin(Omega)*cos(omega)*cos(i), sin(Omega)*sin(i);
	sin(Omega)*cos(omega) + cos(Omega)*sin(omega)*cos(i), -sin(Omega)*sin(omega) + cos(Omega)*cos(omega)*cos(i), -cos(Omega)*sin(i);
	sin(omega)*sin(i),                          cos(omega)*sin(i),                          cos(i)];
	r = Rmat * r_pf;
	v = Rmat * v_pf;
	sv = SpaceFlightDynamics.StateVectors(r, v);
end
