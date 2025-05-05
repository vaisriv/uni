%% +SpaceFlightDynamics/stumpff_C3.m
function C3 = stumpff_C3(z)
	if z > 0
		C3 = (sqrt(z) - sin(sqrt(z))) / (z*sqrt(z));
	elseif z < 0
		C3 = (sinh(sqrt(-z)) - sqrt(-z)) / ((-z)*sqrt(-z));
	else
		C3 = 1/6;
	end
end
