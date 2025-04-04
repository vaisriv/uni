import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# Failure times data
data = np.array([65, 85, 90, 95, 340, 405, 555, 575])
n = len(data)

# Estimate lambda by sample mean
lambda_hat = 1.0 / np.mean(data)

# Use median ranks for empirical CDF
sorted_data = np.sort(data)
# Using (i-0.3)/(n+0.4) as median rank estimates
F_emp = (np.arange(1, n+1) - 0.3) / (n + 0.4)

# Transform for exponential probability plot: Y = ln(-ln(1-F))
Y = np.log(-np.log(1 - F_emp))
X = np.log(sorted_data)

# Linear regression to check linearity
slope, intercept, r_value, p_value, std_err = st.linregress(X, Y)

plt.figure(figsize=(8,6))
plt.plot(X, Y, 'o', label='Data')
plt.plot(X, intercept + slope*X, 'r--', label=f'Fit: slope={slope:.2f}')
plt.xlabel('ln(Time)')
plt.ylabel('ln(-ln(1-F))')
plt.title('Exponential Probability Plot')
plt.legend()
plt.show()

print("Estimated lambda =", lambda_hat)
