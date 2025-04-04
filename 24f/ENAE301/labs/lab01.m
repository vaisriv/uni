l = 0.1 % m
[t,y]= ode45(@myodefun,[0 10],[pi/2 0],[],9.81,l);
plot(t,y);

axis(0.4*[-1 1 -1 1]); hold on
h = [];
for ii=1:length(t)
    delete(h)
    h = plot([0 l*sin(y(ii,1))],[0 -l*cos(y(ii,1))],"o-");
    drawnow
end
