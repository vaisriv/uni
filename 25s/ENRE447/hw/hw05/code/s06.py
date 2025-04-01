import numpy as np
import matplotlib.pyplot as plt

times = np.array([0.693, 1.099, 1.386, 1.609, 1.792])
weib = np.array([-3.35, -2.605, -1.625, -0.786, -0.124])

n = len(times)

a, b = np.polyfit(times, weib, 1)

plt.figure(figsize=(8, 5))
plt.plot(times, a*times+b, label='Line of Best Fit', color = "blue")
plt.scatter(times, weib, color = "red")
plt.title('Weibull Distribution Plot')
plt.legend()
plt.grid(True)
plt.show()

plt.savefig("25s/ENRE447/hw/hw05/images/s06a.png")