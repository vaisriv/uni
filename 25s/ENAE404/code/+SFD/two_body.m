function du = two_body(t, u, mu)
%TWO_BODY ODE for the 2BP
	if nargin < 3
		mu = SFD.mu_Earth();
	end
	du = zeros(6,1);
	du(1:3) = u(4:6);
	r = u(1:3);
	r_norm = norm(r);
	du(4:6) = -mu*r/(r_norm^3);
end
