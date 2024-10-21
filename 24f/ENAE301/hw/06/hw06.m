l0 = 0.5;

xp0 = l0 / 2;
xq0 = xp0 + l0;
dxp0 = 0;
dxq0 = 0;

y0 = [xp0; xq0; dxp0; dxq0];

tspan = [0 600];

[t, y] = ode45(@odefun, tspan, y0);

xp = y(:, 1);
xq = y(:, 2);

figure;
plot(t, xp, 'b-', 'LineWidth', 1.5); hold on;
plot(t, xq, 'r--', 'LineWidth', 1.5);
xlabel('Time [s]');
ylabel('Position [m]');
title('Positions [m] of m_p and m_q over Time [s]');
legend('m_p: Mass M [kg]', 'm_q: Mass m [kg]', 'Location', 'Best');
grid on;

function ode = odefun(~, y)
    M = 10;
    m = 2;
    k = 0.5;
    b = 0.2;
    l0 = 0.5;

    xp = y(1);
    xq = y(2);
    dxp = y(3);
    dxq = y(4);
    
    ddxp = (-b * dxp - 2 * k * xp + k * xq) / M;
    ddxq = (-k * xq + k * xp + k * l0) / m;
    
    ode = [dxp; dxq; ddxp; ddxq];
end