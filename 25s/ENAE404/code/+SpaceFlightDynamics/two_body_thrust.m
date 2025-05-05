%% +SpaceFlightDynamics/two_body_thrust.m
function du = two_body_thrust(t, u, params)
	mu = params(1);
	T_spec = params(2);
	du = zeros(6,1);
	du(1:3) = u(4:6);
	r = u(1:3);
	v = u(4:6);
	r_norm = norm(r);
	grav_acc = -mu*r/(r_norm^3);
	v_norm = norm(v);
	if v_norm > 0
		thrust_acc = T_spec*1e3*(v/v_norm);
	else
		thrust_acc = zeros(3,1);
	end
	du(4:6) = grav_acc + thrust_acc;
end
