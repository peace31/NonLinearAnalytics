#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:42:28 2018

@author: dominiquekatthain
"""
def f(x):
    return x**2 - 9

def gradient(x):
    return 2*x

def Newton_Raphson(f, dfdx, x, eps):
    while abs(f(x)) > eps:
        x = x - float(f(x))/dfdx(x)
    return x
x0 = float(input("Input an initial value:"))
tol = float(input ("input the tolerance:"))
print("Result: ", Newton_Raphson(f, gradient, x0, tol))