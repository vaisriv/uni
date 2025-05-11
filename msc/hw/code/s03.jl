using Plots

α = rand(10)
β = rand(10)

@show α
@show β

scatter(α, β)
savefig("./images/s03.png")
gui()
