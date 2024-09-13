x0 = [0; 0];
tspan = [0 10];
[t, x] = ode45(@harmonic_oscillator, tspan, x0);

figure;
subplot(2,1,1);
plot(t, x(:,1), 'b', 'LineWidth', 2);
xlabel('Time (s)');
ylabel('Displacement x(t) (m)');
title('Displacement vs. Time');
legend('x(t)');

subplot(2,1,2);
plot(t, x(:,2), 'r', 'LineWidth', 2);
xlabel('Time (s)');
ylabel('Velocity \dot{x}(t) (m/s)');
title('Velocity vs. Time');
legend('\dot{x}(t)');

grid on;

function dxdt = harmonic_oscillator(t, x)
    a = 1;
    m = 0.5;
    k = 3;
    dxdt = zeros(2,1);
    dxdt(1) = x(2);
    dxdt(2) = a - (k/m)*x(1);
end