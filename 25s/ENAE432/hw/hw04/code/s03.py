import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the transfer functions.
sys1 = sp.signal.TransferFunction([24], [1, 4])
sys2 = sp.signal.TransferFunction([3], [2, 1, 2])
sys3 = sp.signal.TransferFunction([24], [1, 0.4, 2])

# Define overall simulation time
t_end = 60  # seconds
t = np.linspace(0, t_end, 6000)

# Define the switch activation times.
# We choose:
#   Switch 3 first at t = 0 (since its overshoot is nearly 20 A if thrown later),
#   then Switch 2 at t = 20 s,
#   then Switch 1 at t = 36 s.
t3_on = 0
t2_on = 20
t1_on = 36

# For each switch, we compute its step response starting from its activation time.
# -- Switch 3 response (active from t=0)
t_sys3 = np.linspace(0, t_end - t3_on, 6000)
t3_resp, y3_resp = sp.signal.step(sys3, T=t_sys3)
y3 = np.interp(t - t3_on, t_sys3, y3_resp)

# -- Switch 2 response (active from t = t2_on)
t_sys2 = np.linspace(0, t_end - t2_on, 6000)
t2_resp, y2_resp = sp.signal.step(sys2, T=t_sys2)
y2 = np.zeros_like(t)
mask2 = t >= t2_on
y2[mask2] = np.interp(t[mask2] - t2_on, t_sys2, y2_resp)

# -- Switch 1 response (active from t = t1_on)
t_sys1 = np.linspace(0, t_end - t1_on, 6000)
t1_resp, y1_resp = sp.signal.step(sys1, T=t_sys1)
y1 = np.zeros_like(t)
mask1 = t >= t1_on
y1[mask1] = np.interp(t[mask1] - t1_on, t_sys1, y1_resp)

# Total cumulative current is the sum of all individual responses.
y_total = y3 + y2 + y1

# Plot the cumulative current response.
plt.figure(figsize=(10, 6))
plt.plot(t, y_total, label=r'Cumulative Current $I(t)$', color='blue')
plt.xlabel(r'Time $t$ [s]', fontsize=14)
plt.ylabel(r'Current $I$ [A]', fontsize=14)
plt.title('Cumulative Current Response for Switch Sequence', fontsize=16)

# Mark the maximum load with a horizontal dashed line and annotate.
plt.axhline(20, color='red', linestyle='--', label='Maximum AC Load')
plt.text(4, 19, r'Maxiumum AC Load ($20\,A$)', color='red', fontsize=12)

# Mark the activation times with vertical dashed lines and annotate.
plt.axvline(t3_on, color='green', linestyle='--', label='Switch 3 ON')
plt.axvline(t2_on, color='green', linestyle='--', label='Switch 2 ON')
plt.axvline(t1_on, color='green', linestyle='--', label='Switch 1 ON')

plt.text(t3_on + 1, 2, r'Switch 3 ($I=12\,[\text{A}]$ steady)', color='green', fontsize=12)
plt.text(t2_on + 1, 8, r'Switch 2 ($I=1.5\,[\text{A}]$ steady)', color='green', fontsize=12)
plt.text(t1_on + 1, 12, r'Switch 1 ($I=6\,[\text{A}]$ steady)', color='green', fontsize=12)

# Label the frequencies
plt.text(t3_on + 2, 6, r'$\omega=1.40\,[\text{Hz}]$', color='blue', fontsize=12)
plt.text(t2_on + 2, 12, r'$\omega=0.986\,[\text{Hz}]$', color='blue', fontsize=12)

plt.grid(True)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
