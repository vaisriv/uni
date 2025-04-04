function ydot = myodefun(t,y,g,L)
    ydot(1,1) = y(2);
    ydot(2,1) = -g/L*sin(y(1));
end