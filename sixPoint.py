import numpy as np
import matplotlib.pyplot as plt


def six_point_average(a):
    res = []
    for i in range(len(a)):
        avg = 0
        if i < 5:
            avg = sum(a[0 : i + 1]) / (i + 1)
        else:
            avg = sum(a[i - 5 : i + 1]) / 6

        res.append(avg)

    return res


def six_point_diff(a):
    res = []
    for i in range(len(a)):
        if i < 6:
            res.append(0)
        else:
            res.append(a[i] - a[i - 6])

    return res


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = np.arange(len(a))

avg = six_point_average(a)
diff = six_point_diff(a)

plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.stem(n, a)
plt.title("original signal")
plt.xlabel("n")
plt.ylabel("signal")

plt.subplot(3, 1, 2)
plt.stem(n, avg)
plt.title("avg signal")
plt.xlabel("n")
plt.ylabel("signal")

plt.subplot(3, 1, 3)
plt.stem(n, diff)
plt.title("diff signal")
plt.xlabel("n")
plt.ylabel("signal")

plt.tight_layout()
plt.show()
