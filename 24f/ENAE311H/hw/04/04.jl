using Unitful # degrees = °

# problem 1
V_int = 0.25u"m^2"
rho_w = 1000u"kg/m^3"

D_1 = 60u"cm"
D_2 = 30u"cm"
v_2 = 10u"m/s"

theta = 90u"°"

m_dot = Unitful.upreferred(rho_w * v_2 * pi/4 * D_2^2)
println(m_dot)

v_1 = Unitful.upreferred(v_2*(D_2/D_1)^2)
println(v_1)

p_1 = Unitful.upreferred(0.5*rho_w*(v_2^2 - v_1^2))
println(p_1)

F_A = Unitful.upreferred(m_dot*(v_2-v_1) - p_1*pi/4*D_1^2)
println(F_A)
