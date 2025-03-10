import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

data = np.array([70, 150, 250, 360, 485, 650, 855, 1130, 1540])

t_grid = np.linspace(0, 1600, 400)

cdf_emp = np.array([np.sum(data <= t) for t in t_grid]) / len(data)

kde = gaussian_kde(data)
pdf_est = kde(t_grid)

R_est = 1 - cdf_emp

h_est = np.divide(pdf_est, R_est, out=np.zeros_like(pdf_est), where=R_est>0)

plt.figure(figsize=(10, 8))

plt.subplot(2,2,1)
plt.step(t_grid, cdf_emp, where='post')
plt.xlabel('Time')
plt.ylabel('CDF')
plt.title('Empirical CDF')

plt.subplot(2,2,2)
plt.plot(t_grid, pdf_est)
plt.xlabel('Time')
plt.ylabel('PDF')
plt.title('Estimated PDF')

plt.subplot(2,2,3)
plt.step(t_grid, R_est, where='post')
plt.xlabel('Time')
plt.ylabel('Reliability')
plt.title('Reliability Function')

plt.subplot(2,2,4)
plt.plot(t_grid, h_est)
plt.xlabel('Time')
plt.ylabel('Hazard Rate')
plt.title('Hazard-Rate Function')

plt.tight_layout()
plt.show()
