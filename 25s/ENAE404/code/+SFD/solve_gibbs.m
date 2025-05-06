function v2 = solve_gibbs(r1, r2, r3, mu)
%SOLVE_GIBBS Solve Gibbs's problem 
% Solver for Gibbs's problem
	if nargin < 4
		mu = SFD.mu_Earth();
	end
	c12 = cross(r1, r2);
	c23 = cross(r2, r3);
	c31 = cross(r3, r1);
	N = c12*norm(r3) + c23*norm(r1) + c31*norm(r2);
	D = c12 + c23 + c31;
	S = r1*(norm(r2) - norm(r3)) + r2*(norm(r3) - norm(r1)) + r3*(norm(r1) - norm(r2));
	v2 = sqrt(mu/(norm(N)*norm(D))) * (cross(D, r2)/norm(r2) + S);
end
