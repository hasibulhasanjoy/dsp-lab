import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 10, 1)
omega1 = np.pi * 0.5
omega2 = np.pi

y1 = np.cos(omega1 * n)
y2 = np.cos(omega2 * n)

plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.stem(n, y1)
plt.grid()

plt.subplot(1, 2, 2)
plt.stem(n, y2)
plt.grid()

plt.tight_layout()
plt.show()
