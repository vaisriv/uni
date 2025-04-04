(* --- Define functions for the magnitudes --- *)
  (* Position magnitude as a function of time *)
  posMag[t_] := Norm[rD[t] /. solDidymos[[1]]];
(* Velocity magnitude as a function of time *)
velMag[t_] := Norm[vD[t] /. solDidymos[[1]]];
(* Acceleration is given by a = -muSun * r/|r|^3, so its magnitude is: \
*)
accMag[t_] := 
  Norm[-muSun*(rD[t] /. solDidymos[[1]])/
     Norm[rD[t] /. solDidymos[[1]]]^3];

(* --- Create subplots --- *)
plotPos = Plot[posMag[t], {t, 0, tmaxDidymos},
   PlotRange -> All,
   AxesLabel -> {"Time (s)", "||r|| (km)"},
   PlotLabel -> "Position Magnitude",
   ImageSize -> Large];
plotVel = Plot[velMag[t], {t, 0, tmaxDidymos},
   PlotRange -> All,
   AxesLabel -> {"Time (s)", "||v|| (km/s)"},
   PlotLabel -> "Velocity Magnitude",
   ImageSize -> Large];
plotAcc = Plot[accMag[t], {t, 0, tmaxDidymos},
   PlotRange -> All,
   AxesLabel -> {"Time (s)", "||a|| (km/s^2)"},
   PlotLabel -> "Acceleration Magnitude",
   ImageSize -> Large];

(* --- Arrange the plots in a grid --- *)
GraphicsRow[{
  {plotPos},
  {plotVel},
  {plotAcc}
  }]
