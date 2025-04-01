import numpy as np
import matplotlib.pyplot as plt

times = np.array([811, 907, 1099, 2290, 2900, 3000, 3300, 4100])
# Event indicator: 1 if the failure (event) is observed, 0 if the observation is right-censored (has a "+")
events = np.array([1, 0, 1, 1, 0, 0, 1, 0])

n = len(times)
cumulative_hazard = np.zeros(n)
cum_hazard = 0 

for i in range(n):
    risk_set = np.sum(times >= times[i])
    if events[i] == 1:
        cum_hazard += 1.0 / risk_set
    cumulative_hazard[i] = cum_hazard

a, b = np.polyfit(times, cumulative_hazard, 1)

plt.figure(figsize=(8, 5))
plt.plot(times, a*times+b, label='Line of Best Fit', color = "blue")
plt.scatter(times, cumulative_hazard, label='Rank Increment Estimate', color = "red")
plt.xlabel('Time')
plt.ylabel('Cumulative Hazard')
plt.title('Rank Increment Plot')
plt.legend()
plt.grid(True)
plt.show()

plt.savefig("25s/ENRE447/hw/hw05/images/s04c.png")
print(a)
print(b)