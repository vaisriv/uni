import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# Failure times (uncensored)
failures = np.array([8, 17, 21, 21, 22, 39, 42, 47])
n_fail = len(failures)

# Compute median ranks using (i - 0.3)/(n + 0.4)
i = np.arange(1, n_fail+1)
F_est = (i - 0.3) / (n_fail + 0.4)

# Transform data for Weibull probability plot
X = np.log(failures)
Y = np.log(-np.log(1 - F_est))

# Linear regression to estimate Weibull parameters
slope, intercept, r_value, p_value, std_err = st.linregress(X, Y)
beta_hat = slope
eta_hat = np.exp(-intercept / beta_hat)

plt.figure(figsize=(8,6))
plt.plot(X, Y, 'o', label='Data')
plt.plot(X, intercept + slope*X, 'r--', label=f'Fit: beta={beta_hat:.2f}, eta={eta_hat:.1f}')
plt.xlabel('ln(Time)')
plt.ylabel('ln(-ln(1-F))')
plt.title('Weibull Probability Plot')
plt.legend()
plt.show()

print("Estimated beta =", beta_hat)
print("Estimated eta =", eta_hat)
