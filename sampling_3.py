import numpy as np
import matplotlib.pyplot as plt

# Continuous time signal xa(t) = 3cos(200πt) + 5sin(600πt) + 10cos(1200πt)
f1, f2, f3 = 100, 300, 600
t = np.linspace(0, 0.01, 1000)

xa_t = (
    3 * np.cos(2 * np.pi * f1 * t)
    + 5 * np.sin(2 * np.pi * f2 * t)
    + 10 * np.cos(2 * np.pi * f3 * t)
)

# Sampling at 2500 Hz
fs_2500 = 2500
ts_2500 = 1 / fs_2500
t_2500 = np.arange(0, 0.01, ts_2500)
xa_2500 = (
    3 * np.cos(2 * np.pi * f1 * t_2500)
    + 5 * np.sin(2 * np.pi * f2 * t_2500)
    + 10 * np.cos(2 * np.pi * f3 * t_2500)
)

# Sampling at 1500 Hz
fs_1500 = 1500
ts_1500 = 1 / fs_1500
t_1500 = np.arange(0, 0.01, ts_1500)
xa_1500 = (
    3 * np.cos(2 * np.pi * f1 * t_1500)
    + 5 * np.sin(2 * np.pi * f2 * t_1500)
    + 10 * np.cos(2 * np.pi * f3 * t_1500)
)

# Sampling at 1200 Hz
fs_1200 = 1200
ts_1200 = 1 / fs_1200
t_1200 = np.arange(0, 0.01, ts_1200)
xa_1200 = (
    3 * np.cos(2 * np.pi * f1 * t_1200)
    + 5 * np.sin(2 * np.pi * f2 * t_1200)
    + 10 * np.cos(2 * np.pi * f3 * t_1200)
)

# Sampling at 600 Hz
fs_600 = 600
ts_600 = 1 / fs_600
t_600 = np.arange(0, 0.01, ts_600)
xa_600 = (
    3 * np.cos(2 * np.pi * f1 * t_600)
    + 5 * np.sin(2 * np.pi * f2 * t_600)
    + 10 * np.cos(2 * np.pi * f3 * t_600)
)

# Plotting
plt.figure(figsize=(14, 10))

# Subplot 1: 2500 Hz
plt.subplot(2, 2, 1)
plt.plot(t, xa_t, label="Continuous", color="blue")
plt.stem(
    t_2500, xa_2500, linefmt="r-", markerfmt="ro", basefmt="k-", label="Sampled @2500Hz"
)
plt.title("Sampling at 2500 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Subplot 2: 1500 Hz
plt.subplot(2, 2, 2)
plt.plot(t, xa_t, label="Continuous", color="blue")
plt.stem(
    t_1500, xa_1500, linefmt="g-", markerfmt="go", basefmt="k-", label="Sampled @1500Hz"
)
plt.title("Sampling at 1500 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Subplot 3: 1200 Hz
plt.subplot(2, 2, 3)
plt.plot(t, xa_t, label="Continuous", color="blue")
plt.stem(
    t_1200, xa_1200, linefmt="m-", markerfmt="mo", basefmt="k-", label="Sampled @1200Hz"
)
plt.title("Sampling at 1200 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Subplot 4: 600 Hz
plt.subplot(2, 2, 4)
plt.plot(t, xa_t, label="Continuous", color="blue")
plt.stem(
    t_600, xa_600, linefmt="c-", markerfmt="co", basefmt="k-", label="Sampled @600Hz"
)
plt.title("Sampling at 600 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.suptitle(
    "Continuous vs Sampled Signal at Different Frequencies", fontsize=16, y=1.03
)
plt.show()
