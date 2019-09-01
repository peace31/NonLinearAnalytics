#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:42:28 2018

@author: dominiquekatthain
"""
def f(x):
    return x**2 - 9
def secant(f, x0, x1, eps,maxiter):
    f_value0 = f(x0)
    f_value1 = f(x1)
    iter_num= 0
    x=x0
    while abs(f_value1) > eps and iter_num < maxiter:
        try:
            val = float(f_value1 - f_value0)/(x1 - x0)
            x = x1 - float(f_value1)/val
        except ZeroDivisionError:
            print ("Error!:divided by zero for x = ", x)
            return x
        x0 = x1
        x1 = x
        f_value0 = f_value1
        f_value1 = f(x1)
        iter_num += 1
    return x
x0 = float(input("Input an initial value:"))
x1 = float(input("Input an initial value:"))
tol = float(input ("input the tolerance:"))
maxiter = int(input("maximum number of itterations"))
solution = secant(f, x0, x1, tol,maxiter)
print("Result: ", solution)
