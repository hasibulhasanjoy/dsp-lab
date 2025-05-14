import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 11, 1)
u_n = np.where(n >= 0, 1, 0)
ramp = np.where(n >= 0, n, 0)
A = 1
B = 0.5
t = np.linspace(0, 10, 500)
y = A * np.exp(B * t)

x = np.linspace(0, 2 * np.pi, 500)
y1 = np.sin(x)
y2 = np.cos(x)

plt.subplot(3, 2, 1)
plt.stem(n, u_n, label="unit step sequence")
plt.xlabel("n", color="red")
plt.ylabel("u_n", color="green")
plt.legend()
plt.grid()
# plt.show()

plt.subplot(3, 2, 2)
plt.scatter(n, ramp)
plt.stem(n, ramp, label="ramp sequence")
plt.xlabel("n")
plt.ylabel("ramp")
plt.legend()
plt.grid()
# plt.show()

plt.subplot(3, 2, 3)
plt.plot(t, y, label="Exponential")
plt.xlabel("t(n)")
plt.ylabel("y(n)")
plt.legend()
plt.grid()
# plt.show()

plt.subplot(3, 2, 4)
plt.plot(x, y1, label="sin wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend(loc="best")
plt.title("sine wave")
plt.grid()
plt.axhline(y=0)
plt.axvline(x=0)
# plt.show()

plt.subplot(3, 2, 5)
plt.plot(x, y2, label="cos wave")
plt.xlabel("x")
plt.ylabel("A")
plt.legend(loc="best")
plt.title("cos wave")
plt.grid()
plt.axhline(y=0)
plt.axvline(x=0)

plt.tight_layout()
plt.show()
