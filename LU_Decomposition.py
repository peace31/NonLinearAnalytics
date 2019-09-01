#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:42:28 2018

@author: dominiquekatthain
"""
import numpy
from scipy import *
def lu(Origin_matrix,eps):

    m=len(Origin_matrix)
    n=len(Origin_matrix[0])
    for i in range(0,n):
        p = Origin_matrix[i,i]
        if abs(p) >= eps:
            for k in range(i+1,n):
                Origin_matrix[k,i] = Origin_matrix[k,i]/p
                Origin_matrix[k,i+1:n] = Origin_matrix[k,i+1:n] - Origin_matrix[k,i]*Origin_matrix[i,i+1:n]
    L = eye(n)+tril(Origin_matrix,-1)
    U = triu(Origin_matrix)
    return L,U


A = numpy.array([[2,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,2]])
tol = float(input ("input the tolerance:"))
L,U = lu(A,tol)
print("original matrix=",A)
print ("L=",L)
print("U=",U)