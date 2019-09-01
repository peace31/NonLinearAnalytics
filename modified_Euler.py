import matplotlib.pyplot as plt
import numpy as np


def feval(funcName, *args):
    return eval(funcName)(*args)


def modifiedEuler(func, yinit, x_range, h):
    m = len(yinit)
    n = int((x_range[-1] - x_range[0]) / h)

    x = x_range[0]
    y = yinit

    # Containers for solutions
    xsol = np.empty(0)
    xsol = np.append(xsol, x)

    ysol = np.empty(0)
    ysol = np.append(ysol, y)

    for i in range(n):
        k1 = feval(func, x, y)

        ypredictor = y + k1 * h

        k2 = feval(func, x + h, ypredictor)

        for j in range(m):
            y[j] = y[j] + (h / 2) * (k1[j] + k2[j])

        x = x + h
        xsol = np.append(xsol, x)

        for r in range(len(y)):
            ysol = np.append(ysol, y[r])

    return [xsol, ysol]


def myFunc(x, y):
    dy = np.zeros((len(y)))
    dy[0] = np.exp(-2 * x) - 2 * y[0]
    return dy


# -----------------------

h = 0.2
x = np.array([0, 2])
yinit = np.array([1.0 / 10])

[ts, ys] = modifiedEuler('myFunc', yinit, x, h)

dt = int((x[-1] - x[0]) / h)
t = [x[0] + i * h for i in range(dt + 1)]
yexact = []
for i in range(dt + 1):
    ye = (1.0 / 10) * np.exp(-2 * t[i]) + t[i] * np.exp(-2 * t[i])
    yexact.append(ye)

plt.plot(ts, ys, 'r')
plt.plot(t, yexact, 'b')
plt.xlim(x[0], x[1])
plt.legend(["Modified Euler Solution", "Exact solution"], loc=1)
plt.xlabel('x', fontsize=17)
plt.ylabel('y', fontsize=17)
plt.tight_layout()
plt.show()