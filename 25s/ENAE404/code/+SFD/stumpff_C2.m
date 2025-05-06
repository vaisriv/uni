function C2 = stumpff_C2(z)
%STUMPFF_C2 Stumpff Constant calculator for use in solving Lambert's
%problem
	if z > 0
		C2 = (1 - cos(sqrt(z)))/z;
	elseif z < 0
		C2 = (cosh(sqrt(-z)) - 1)/(-z);
	else
		C2 = 1/2;
	end
end
