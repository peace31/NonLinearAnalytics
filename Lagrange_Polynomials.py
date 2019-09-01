#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:42:28 2018

@author: dominiquekatthain
"""
import numpy as np
def LagrangeInterp(xn,yn):
    n = len(xn)
    out = [0.0] * (n)
    def B_vector(k, xi):
        """Calculate b_j(x_xi)"""
        val = 1.0
        for i in range(n):
            if i != k:
                val *= (xi - xn[i]) / (xn[k] - xn[i])
        return val
    for i, xi in enumerate(xn):
        # Construct each element of L(x)
        for k in range(n):
            out[i] += yn[k] * B_vector(k, xi)
    return out
def f(x):
    return np.cos(np.sin(np.pi*x))
a = float(input("Input a value:"))
b = float(input("Input b value:"))
n = int(input("Input n value:"))
xn = np.linspace(a, b, n)
yn = f(xn)
Yn = LagrangeInterp(xn,yn)
print("Real Result: ", yn)
print("Interpolation Result: ", Yn)
