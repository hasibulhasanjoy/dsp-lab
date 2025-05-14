import numpy as np
import matplotlib.pyplot as plt


def cross_corelation(x, y):
    res = []
    N = len(x)
    for k in range(-(N - 1), N):
        val = 0
        for n in range(N):
            if 0 <= n - k < N:
                val += x[n] * y[n - k]
        res.append(int(val))

    return res


x = np.array([1, 3, -2, 4])
y = np.array([2, 3, -1, 3])
z = np.array([2, -1, 4, -2])

r_xy = cross_corelation(x, y)
r_yz = cross_corelation(y, z)
lags = np.arange(-len(x) + 1, len(x))

# Plot the Results
plt.figure(figsize=(12, 5))

# Plot r_xy
plt.subplot(1, 2, 1)
plt.stem(lags, r_xy)
plt.title("Cross-Correlation: x(n) vs y(n)")
plt.xlabel("Lag")
plt.axvline(color="red")
plt.axhline(color="red")
plt.ylabel("Correlation")
plt.grid(True)

# Plot r_yz
plt.subplot(1, 2, 2)
plt.stem(lags, r_yz)
plt.title("Cross-Correlation: y(n) vs z(n)")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.axvline(color="red")
plt.axhline(color="red")
plt.grid(True)

plt.tight_layout()
plt.show()
