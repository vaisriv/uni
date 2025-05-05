%% +SpaceFlightDynamics/solve_2BP.m
function sv_array = solve_2BP(initial, tspan, mu, reltol, abstol, int_pts)
	if nargin < 6
		int_pts = 2;
	end
	if nargin < 5
		abstol = 1e-9;
	end
	if nargin < 4
		reltol = 1e-9;
	end
	if nargin < 3
		mu = SpaceFlightDynamics.muEarth();
	end
	u0 = [initial.r; initial.v];
	sol = ode45(@(t,u) SpaceFlightDynamics.two_body(t,u,mu), tspan, u0, odeset('RelTol',reltol,'AbsTol',abstol));
	t_int = linspace(tspan(1), tspan(2), int_pts);
	y = deval(sol, t_int);
	sv_array(int_pts) = SpaceFlightDynamics.StateVectors();
	for i = 1:int_pts
		r = y(1:3,i);
		v = y(4:6,i);
		sv_array(i) = SpaceFlightDynamics.StateVectors(r, v);
	end
end
