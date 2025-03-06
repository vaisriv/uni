import numpy as np
import matplotlib.pyplot as plt

data = np.array(
    [4, 7, 8, 12, 19, 27, 50, 65, 66, 69, 71, 73, 75, 91, 107, 115, 142, 166, 184, 192]
)
data_sorted = np.sort(data)
N = len(data_sorted)

# Histogram
plt.hist(data, bins="auto", edgecolor="black")
plt.xlabel("Time to Failure (hours)")
plt.ylabel("Frequency")
plt.title("Histogram of Failure Times")
plt.show()

# CDF
cdf = np.arange(1, N + 1) / float(N)

plt.figure(figsize=(8, 5))
plt.step(data_sorted, cdf, where='post', label='Empirical CDF')
plt.xlabel('Time to Failure (hours)')
plt.ylabel('Cumulative Probability')
plt.title('Empirical CDF of Failure Times')
plt.grid(True)
plt.legend()
plt.show()
