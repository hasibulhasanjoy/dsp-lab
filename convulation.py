import numpy as np
import matplotlib.pyplot as plt


def my_convolution(x, h):
    y = []

    x_len = len(x)
    h_len = len(h)
    y_len = x_len + h_len - 1

    for n in range(y_len):
        val = 0
        for k in range(x_len):
            if n - k >= 0 and n - k < h_len:
                val += x[k] * h[n - k]
        y.append(int(val))

    return y


n = np.arange(0, 21)
x = np.ones_like(n)
h = np.concatenate((np.ones(5), np.zeros(len(n) - 5)))
y = np.convolve(x, h)
my_y = my_convolution(x, h)
n_y = np.arange(0, len(y))

# plot signal
plt.figure(figsize=(12, 6))
# x(n)
plt.subplot(3, 1, 1)
plt.stem(n, x)
plt.xticks(n)
plt.title("x(n)")
plt.xlabel("n")
plt.ylabel("x(n)")

# h(n)
plt.subplot(3, 1, 2)
plt.stem(n, h)
plt.xticks(n)
plt.title("h(n)")
plt.xlabel("n")
plt.ylabel("h(n)")

# h(n)
plt.subplot(3, 1, 3)
plt.stem(n_y, my_y)
plt.xticks(n_y)
plt.title("y(n)")
plt.xlabel("n")
plt.ylabel("y(n)")

plt.tight_layout()
plt.show()
