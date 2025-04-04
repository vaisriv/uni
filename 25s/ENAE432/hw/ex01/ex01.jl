# Set given parameters
a = 2.08
b = 2.98
c = 5.53

# Characteristic equation: a*r^2 + b*r + c = 0
# Discriminant
disc = b^2 - 4*a*c

println("Discriminant = ", disc)

if disc < 0
    println("The system is underdamped, disc < 0")
else
    println("The system is not underdamped, disc >= 0")
end

# Compute the damped frequency (imag part of roots)
omega_d = sqrt(4*a*c - b^2) / (2*a)  # same as sqrt(c/a - (b/(2a))^2)

println("Damped angular frequency = ", omega_d, " rad/s")