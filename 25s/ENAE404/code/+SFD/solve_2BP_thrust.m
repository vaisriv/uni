function sv_array = solve_2BP_thrust(initial, tspan, mu, T_spec, reltol, abstol, int_pts)
%SOLVE_2BP_THRUST Solve the 2BP Problem in the case where the SpaceCraft
%has Thrust
	if nargin < 7
		int_pts = 2;
	end
	if nargin < 6
		abstol = 1e-9;
	end
	if nargin < 5
		reltol = 1e-9;
	end
	if nargin < 4
		T_spec = 1e-4;
	end
	if nargin < 3
		mu = SFD.mu_Earth();
	end
	u0 = [initial.r; initial.v];
	sol = ode45(@(t,u) SFD.two_body_thrust(t,u,[mu,T_spec]), tspan, u0, odeset('RelTol',reltol,'AbsTol',abstol));
	t_int = linspace(tspan(1), tspan(2), int_pts);
	y = deval(sol, t_int);
	sv_array(int_pts) = SFD.StateVectors();
	for i = 1:int_pts
		r = y(1:3,i);
		v = y(4:6,i);
		sv_array(i) = SFD.StateVectors(r, v);
	end
end
