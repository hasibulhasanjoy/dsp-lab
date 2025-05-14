import numpy as np
import matplotlib.pyplot as plt

f = 5
t = np.linspace(0, 1, 1000)
x_t = np.sin(2 * np.pi * f * t)

f_s = 40
t_s = 1 / f_s
t_count = np.arange(0, 1, t_s)
x_n = np.sin(2 * np.pi * f * t_count)

# continuous time signal
plt.figure(figsize=(10, 5))
plt.plot(t, x_t, label="continuous time signal")
plt.stem(t_count, x_n, label="discreet time signal", linefmt="r-", markerfmt="ro")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend()
plt.grid()
plt.axhline(y=0, color="black")
plt.axvline(x=0, color="black")
plt.show()
