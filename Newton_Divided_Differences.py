#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:42:28 2018

@author: dominiquekatthain
"""
import numpy as np
# import matplotlib.pylab as plt
def NDD(xn,yn, xnn):
    n = len(xn)
    nx = len(xnn)
    N = [0.0] * (nx)
    def A_val(n1, n2=None):
        if n2 is None: n2 = n1; n1 = 0
        if n1 == n2:
            return yn[n1]
        elif n2 - n1 == 1:
            return (yn[n2] - yn[n1]) / (xn[n2] - xn[n1])
        else:
            return (A_val(n1 + 1, n2) - A_val(n1, n2 - 1)) / (xn[n2] - xn[n1])
    def v_value(nn, xi):
        v = 1.0
        for i in range(0, nn):
            v *= float(xi - xn[i])
        return v
    # Construct N(x)
    for i in range(nx):
        for j in range(0, n):
            N[i] += A_val(j) * v_value(j, xnn[i])
    return N
def f(x):
    return np.cos(np.sin(np.pi*x))
a = float(input("Input a value:"))
b = float(input("Input b value:"))
n = int(input("Input n value:"))
p = int(input("Input p value:"))
xn = np.linspace(a, b, n)
yn = f(xn)
xnn=np.linspace(a, b, p)
ynn = NDD(xn,yn, xnn)
print("x value:",xn)
print("y value:",yn)
print("interpol x value:",xnn)
print("interpol y value:",ynn)
# plt.plot(xn, yn, 'r')
# plt.plot(xnn,ynn, 'k')
# plt.show()