(* Define constants *)
x0 = 0.25;
initialPosition = 0.4;
k = 1;
c = 5;
m = 1;

(* Linear spring equation *)
linearSpring = {x''[t] + (k/m)*(x[t] - x0) == 0, x[0] == initialPosition, x'[0] == 0};

(* Nonlinear spring equation *)
nonlinearSpring = {x''[t] + (k/m)*(x[t] - x0) + (c/m)*(x[t] - x0)^3 == 0, x[0] == initialPosition, x'[0] == 0};

(* Time range *)
timeRange = {t, 0, 20};

(* Solve the equations numerically *)
linearSolution = NDSolve[linearSpring, x, timeRange];
nonlinearSolution = NDSolve[nonlinearSpring, x, timeRange];

(* Plot the results *)
Plot[{Evaluate[x[t] /. linearSolution], Evaluate[x[t] /. nonlinearSolution]}, {t, 0, 20},
 PlotLegends -> {"Linear Spring", "Nonlinear Spring"},
 AxesLabel -> {"Time (s)", "Position (m)"}, PlotStyle -> {Blue, Red}]
