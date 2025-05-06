classdef StateVectors
%STATEVECTORS Named Tuple of State Vectors
	properties
		r % 3x1 position vector
		v % 3x1 velocity vector
	end
	methods
		function obj = StateVectors(r,v)
			obj.r = r;
			obj.v = v;
		end
	end
end
