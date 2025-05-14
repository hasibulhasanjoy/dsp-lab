import numpy as np
import matplotlib.pyplot as plt

# continuous time signal: x(t) = 3cos(2 * pi * 50 * t)
A = 3
f = 50
t = np.linspace(0, 1, 1000)
x_t = A * np.cos(2 * np.pi * f * t)

# sampling in 200Hz
fs1 = 200
ts1 = 1 / fs1
t_count1 = np.arange(0, 1, ts1)
x_n1 = A * np.cos(2 * np.pi * f * t_count1)

# sampling in 75Hz
fs2 = 75
ts2 = 1 / fs2
t_count2 = np.arange(0, 1, ts2)
x_n2 = A * np.cos(2 * np.pi * f * t_count2)

# signal plotting
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x_t, label="continuous time signal")
plt.stem(t_count1, x_n1, linefmt="r-", markerfmt="ro", label="discreet time signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("sampling in 200Hz")
plt.axhline(y=0)
plt.axvline(x=0)
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, x_t, label="continuous time signal")
plt.stem(t_count2, x_n2, linefmt="r-", markerfmt="ro", label="discreet time signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("sampling in 75Hz")
plt.axhline(y=0)
plt.axvline(x=0)
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
