% Define the given pressure and shear stress distributions
p_u = @(x) 2e4 * (x - 1) + 2.7e4;  % Pressure on the upper surface
p_l = @(x) 1e4 * (x - 1) + 1.1e5;  % Pressure on the lower surface
tau_u = @(x) 144 * x.^(-0.3);       % Shear stress on the upper surface
tau_l = @(x) 360 * x.^(-0.3);       % Shear stress on the lower surface

% Chord length and angle of attack (in radians)
c = 1;  % Chord length in meters
alpha = deg2rad(15);  % Convert angle of attack to radians

% Normal force (F_n) - due to pressure difference
F_n = integral(@(x) (p_l(x) - p_u(x)), 0, c);

% Axial force (F_a) - due to shear stress
F_a = integral(@(x) (tau_l(x) + tau_u(x)), 0, c);

% Lift (L) and Drag (D) - based on normal and axial forces
L = F_n * cos(alpha) - F_a * sin(alpha);
D = F_n * sin(alpha) + F_a * cos(alpha);

% Moment about the Leading Edge (LE)
M_LE = integral(@(x) x .* (p_l(x) - p_u(x)), 0, c);

% Moment about the quarter chord (1/4 chord is at x = 0.25)
M_quarter_chord = integral(@(x) (x - 0.25) .* (p_l(x) - p_u(x)), 0, c);

% Center of Pressure (x_COP) - based on moment about the LE
x_COP = M_LE / F_n;

% Display the results
fprintf('Normal Force (F_n): %.2f N/m\n', F_n);
fprintf('Axial Force (F_a): %.2f N/m\n', F_a);
fprintf('Lift (L): %.2f N/m\n', L);
fprintf('Drag (D): %.2f N/m\n', D);
fprintf('Moment about Leading Edge (M_LE): %.2f Nm/m\n', M_LE);
fprintf('Moment about Quarter Chord (M_1/4): %.2f Nm/m\n', M_quarter_chord);
fprintf('Center of Pressure (x_COP): %.2f m\n', x_COP);
