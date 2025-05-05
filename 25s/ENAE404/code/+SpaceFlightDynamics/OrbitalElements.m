%% +SpaceFlightDynamics/OrbitalElements.m
classdef OrbitalElements
	properties
		a
		e
		i_deg
		Omega_deg
		omega_deg
		nu_deg
	end
	methods
		function obj = OrbitalElements(a,e,i_deg,Omega_deg,omega_deg,nu_deg)
			obj.a = a;
			obj.e = e;
			obj.i_deg = i_deg;
			obj.Omega_deg = Omega_deg;
			obj.omega_deg = omega_deg;
			obj.nu_deg = nu_deg;
		end
	end
end
