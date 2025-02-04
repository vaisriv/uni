(* Define the Sun's gravitational parameter (km^3/s^2) *)
muSun = 1.32712*10^11;

(* Solve the two\[Hyphen]body ODE in vector form:
   r'(t) = v(t)
   v'(t) = -muSun * r(t)/Norm[r(t)]^3
   where r(t) is a 3\[Hyphen]vector {x,y,z}. *)

(* ----- Earth ----- *)
initEarth = {
  (* initial position: *) {6.825*10^7, 1.30864*10^8, 1.81329*10^4},
  (* initial velocity: *) {-26.7639, 13.8981, -9.22784*10^-4}
};
tmaxEarth = 7.0*10^7;  (* time span in seconds *)

solEarth = NDSolve[
  {
    rE'[t] == vE[t],
    vE'[t] == -muSun*rE[t]/Norm[rE[t]]^3,
    rE[0] == initEarth[[1]],
    vE[0] == initEarth[[2]]
  },
  {rE, vE},
  {t, 0, tmaxEarth}
];

(* ----- Didymos ----- *)
initDidymos = {
  (* initial position: *) {-2.39573*10^8, -2.35661*10^8, 9.54384*10^6},
  (* initial velocity: *) {12.4732, -9.74427, -0.87661}
};
tmaxDidymos = 7.0*10^7;

solDidymos = NDSolve[
  {
    rD'[t] == vD[t],
    vD'[t] == -muSun*rD[t]/Norm[rD[t]]^3,
    rD[0] == initDidymos[[1]],
    vD[0] == initDidymos[[2]]
  },
  {rD, vD},
  {t, 0, tmaxDidymos}
];

(* ----- DART ----- *)
initDART = {
  (* initial position: *) {6.82409*10^7, 1.30854*10^8, 1.52197*10^4},
  (* initial velocity: *) {-30.6997, 8.11796, 3.95772}
};
tmaxDART = 26*10^6;

solDART = NDSolve[
  {
    rA'[t] == vA[t],
    vA'[t] == -muSun*rA[t]/Norm[rA[t]]^3,
    rA[0] == initDART[[1]],
    vA[0] == initDART[[2]]
  },
  {rA, vA},
  {t, 0, tmaxDART}
];

(* Create 3D parametric plots for each trajectory *)
trajEarth = ParametricPlot3D[
  Evaluate[rE[t] /. solEarth],
  {t, 0, tmaxEarth},
  PlotStyle -> {Blue, Thick},
  Mesh -> None
];

trajDidymos = ParametricPlot3D[
  Evaluate[rD[t] /. solDidymos],
  {t, 0, tmaxDidymos},
  PlotStyle -> {Red, Thick},
  Mesh -> None
];

trajDART = ParametricPlot3D[
  Evaluate[rA[t] /. solDART],
  {t, 0, tmaxDART},
  PlotStyle -> {Green, Thick},
  Mesh -> None
];

(* Optional: Add labels at the endpoints of each trajectory *)
earthLabel = Graphics3D[{
    Blue,
    Text[Style["Earth", Bold, 14],
      Evaluate[rE[tmaxEarth] /. solEarth]]
}];
didymosLabel = Graphics3D[{
    Red,
    Text[Style["Didymos", Bold, 14],
      Evaluate[rD[tmaxDidymos] /. solDidymos]]
}];
dartLabel = Graphics3D[{
    Green,
    Text[Style["DART", Bold, 14],
      Evaluate[rA[tmaxDART] /. solDART]]
}];

(* Combine the trajectories and labels into one 3D plot *)
Show[
  trajEarth, trajDidymos, trajDART,
  earthLabel, didymosLabel, dartLabel,
  Axes -> True,
  AxesLabel -> {"x (km)", "y (km)", "z (km)"},
  Boxed -> True,
  ImageSize -> Large,
  PlotRange -> All,
  ViewPoint -> {1.3, -2.4, 1.5}
]
