(* Specific angular momentum vector and its components *)
h[t_] := Cross[rDsol[t], vDsol[t]];
hMag[t_] := Norm[h[t]];
hX[t_] := h[t][[1]];
hY[t_] := h[t][[2]];
hZ[t_] := h[t][[3]];

(* --- Plot the angular momentum quantities in subplots --- *)
hMagPlot = Plot[
	hMag[t], {t, 0, tmaxDidymos},
	PlotRange -> All,
	AxesLabel -> {"Time (s)", "||h|| (km\.b2/s)"},
	AxesOrigin -> {0,0},
	PlotLabel -> "Angular Momentum Magnitude",
	ImageSize -> Large
];

hXPlot = Plot[
	hX[t], {t, 0, tmaxDidymos},
	PlotRange -> All,
	AxesLabel -> {"Time (s)", "hₓ (km\.b2/s)"},
	AxesOrigin -> {0,0},
	PlotLabel -> "Angular Momentum x Component",
	ImageSize -> Large
];

hYPlot = Plot[
	hY[t], {t, 0, tmaxDidymos},
	PlotRange -> All,
	AxesLabel -> {"Time (s)", "h_y (km\.b2/s)"},
	AxesOrigin -> {0,0},
	PlotLabel -> "Angular Momentum y Component",
	ImageSize -> Large
];

hZPlot = Plot[
	hZ[t], {t, 0, tmaxDidymos},
	PlotRange -> All,
	AxesLabel -> {"Time (s)", "h_z (km\.b2/s)"},
	AxesOrigin -> {0,0},
	PlotLabel -> "Angular Momentum z Component",
	ImageSize -> Large
];

(* Arrange the angular momentum plots in a 2x2 grid *)
angularMomentumGrid = GraphicsGrid[
	{
		{hMagPlot, hXPlot},
		{hYPlot, hZPlot}
	},
	Spacings -> {2, 2}
];

(* --- Display the plots --- *)
Print[angularMomentumGrid];
