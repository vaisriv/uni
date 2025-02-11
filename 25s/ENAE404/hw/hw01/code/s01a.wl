(* Interpolated solutions for position and velocity *)
rDsol[t_] := Evaluate[rD[t] /. solDidymos[[1]]];
vDsol[t_] := Evaluate[vD[t] /. solDidymos[[1]]];

(* Specific energy: kinetic plus potential *)
energy[t_] := 1/2 Norm[vDsol[t]]^2 - muSun/Norm[rDsol[t]];

(* --- Plot the specific energy as a function of time --- *)
energyPlot = Plot[
	energy[t], {t, 0, tmaxDidymos},
	PlotRange -> All,
	AxesLabel -> {"Time (s)", "Specific Energy (km\.b2/s\.b2)"},
	AxesOrigin -> {0,0},
	PlotLabel -> "Specific Energy vs Time",
	ImageSize -> Large
];

(* --- Display the plot --- *)
Print[energyPlot];
