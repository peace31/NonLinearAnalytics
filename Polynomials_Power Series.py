#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:42:28 2018

@author: dominiquekatthain
"""
from numpy import *
import matplotlib.pyplot as plt
def poly_interpolate(xn, yn):
    cc = list()
    for i in range(min(len(xn), len(yn))):
        cc.append(yn[i])
        if i == 0: continue
        Tr = [xn[i]-xn[j] for j in range(i)]
        Tr.insert(0, 1)
        cc[i] /= prod(Tr)
        cc[i] -= sum([c_[k]*Tr[k] for k in range(i)]/prod(Tr))
    def poly(t):
        a = array([t - xn[k] for k in range(min(len(xn), len(yn)))])
        a = concatenate((ones((1, shape(a)[1])), a), axis=0)
        z = list()
        for k in range(a.shape[1]):
            z.append(array([prod(a[:j, k]) for j in range(1, a.shape[0])]).dot(array(cc)))
        return z
    return poly

a = float(input("Input a value:"))
b = float(input("Input b value:"))
n = int(input("Input n value:"))
xn = [-2, -1, 0, 1, 2]
yn = [-5, -3, -15, 39, -9]
interpolated = poly_interpolate(xn, yn)
t = linspace(a, b, n)
plt.plot(t, interpolated(t))
plt.scatter(xn, yn)
plt.show()