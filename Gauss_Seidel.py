#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:42:28 2018

@author: dominiquekatthain
"""
import numpy as np
def Gauss_Seidel(A, b, tol):
    n = len(A)
    U = np.triu(A, 1)
    L = np.tril(A)
    out = np.ones((n, 1))
    error = np.ones((n, 1)) * 100
    while np.max(error) > tol:
        x_val = np.dot(np.linalg.inv(L), (b - np.dot(U, out)))
        error = abs((x_val - out) / x_val) * 100
        out = x_val
    output=[]
    for i in range(len(out)):
        output.append(out[i][0])
    return output
A = np.array([[10,2,-1],[-3,-6,2],[1,2,5]])
b = np.array([[27],[-61.5],[-21.5]])
tol = float(input ("input the tolerance:"))
out=Gauss_Seidel(A, b, tol)
print("Result: ", out)