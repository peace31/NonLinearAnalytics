from math import log
import math
import numpy as np
def linearRegression(pairs):
    """
    y = mx + b
    """
    Sx = Sy = Sxx = Sxy = Syy = 0.0
    n = len(pairs)
    for x,y in pairs:
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Sxy = Sxy + x*y
        Syy = Syy + y*y
    m = ((n * Sxy) - (Sx * Sy)) / ((n * Sxx) - Sx ** 2)
    b = (Sy - (m * Sx)) / n
    r = ((n * Sxy) - (Sx * Sy)) / (math.sqrt((n * (Sxx)) - (Sx ** 2)) *
math.sqrt((n * Syy) - (Sy ** 2)))
    print("y = %sx + %s" % (m, b))
    # print("r = %s" % r)
    return m, b, r
pairs = np.array([[0.5, 8.4],[1.0, 6.7],[1.5, 4.7],[2.0, 3.8]])
linearRegression(pairs)