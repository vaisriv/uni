function C3 = stumpff_C3(z)
%STUMPFF_C3 Stumpff Constant calculator for use in solving Lambert's
%problem
	if z > 0
		C3 = (sqrt(z) - sin(sqrt(z))) / (z*sqrt(z));
	elseif z < 0
		C3 = (sinh(sqrt(-z)) - sqrt(-z)) / ((-z)*sqrt(-z));
	else
		C3 = 1/6;
	end
end
