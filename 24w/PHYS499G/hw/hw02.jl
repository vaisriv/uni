include("../code/PHYS499G.jl")
clc()

X_up_mu_nu = [2 0 1 -1; -1 0 3 2; -1 1 0 0; -2 1 1 -2]
V_up_mu = [-1 2 0 -2]
eta = [-1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1]

X_up_mu_sub_nu = tensor_lower(X_up_mu_nu, eta, "c")
X_up_nu_sub_mu = tensor_lower(X_up_mu_nu, eta, "r")
X_sub_mu_nu = tensor_lower(X_up_mu_sub_nu, eta, "r")

V_sub_mu = tensor_lower(V_up_mu, eta, "r")

X_up_mu_nu_sym = symmetric_part(X_up_mu_nu)

ans_c = X_up_mu_nu_sym
println("ans c:")
display(ans_c)

X_sub_mu_nu_asym = asymmetric_part(X_sub_mu_nu)

ans_d = X_sub_mu_nu_asym
println("ans d:")
display(ans_d)

X_up_nu_sub_mu_trace = tr(X_up_nu_sub_mu)

ans_e = X_up_nu_sub_mu_trace
println("ans e:")
display(ans_e)

ans_f = dot(V_up_mu, V_sub_mu)
println("ans f:")
display(ans_f)

ans_g = V_sub_mu*X_up_mu_nu
println("ans g:")
display(ans_g)