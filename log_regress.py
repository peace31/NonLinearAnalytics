import numpy as np
import matplotlib.pyplot as plt
def logFit(x,y):
    # cache some frequently reused terms
    sumy = np.sum(y)
    sumlogx = np.sum(np.log(x))

    b = (x.size*np.sum(y*np.log(x)) - sumy*sumlogx)/(x.size*np.sum(np.log(x)**2) - sumlogx**2)
    a = (sumy - b*sumlogx)/x.size

    return a,b

x = np.array([4,8,15,29,58,116,231,462,924,1848])
y = np.array([1.05,2.11,3.95,7.37,13.88,25.46,43.03,64.28,81.97,87.43])

def logFunc(x, a, b):
    return a + b*np.log(x)

plt.plot(x, y, ls="none", marker='.')

xfit = np.linspace(1,2000,num=200)
plt.plot(xfit, logFunc(xfit, *logFit(x,y)))
plt.show()