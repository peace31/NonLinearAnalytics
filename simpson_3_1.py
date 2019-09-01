def simpson31(f, a, b, n):
    h=(b-a)/n
    k=0.0
    x=a + h
    for i in range(1,int(n/2) + 1):
        k += 4*f(x)
        x += 2*h

    x = a + 2*h
    for i in range(1,int(n/2)):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)

from math import exp  # or from math import *
def g(t):
    return exp(-t**4)

a = float(input("Input a value:"))#-2
b = float(input("Input b value:"))# 2
n = int(input("Input n value:"))# 1000
result = simpson31(g, a, b, n)
print (result)
