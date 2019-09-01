#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:42:28 2018

@author: dominiquekatthain
"""
def gaussian_elimination(A):
    n = len(A)
    for i in range(n):
        A=calculation(A, n, i)
        for j in range(i + 1, n):
            A[j] = [A[j][k] - A[i][k] * A[j][i] / A[i][i] for k in range(n + 1)]

    if A[n - 1][n - 1] == 0:
        return None
    # backward substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = sum(A[i][j] * x[j] for j in range(i, n))
        x[i] = (A[i][n] - s) / A[i][i]
    return x
def calculation(B, n, i):
    eps = -1e10
    row=0
    for r in range(i, n):
        if eps < abs(B[r][i]):
            row = r
            eps = abs(B[r][i])
    B[i], B[row] = B[row], B[i]
    return B

A = [[0,-2,6,-10], [-1,3,-6,5], [4,-12,8,12]]
print("Result: ",gaussian_elimination(A))
