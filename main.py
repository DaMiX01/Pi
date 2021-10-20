from decimal import *
from math import factorial
 
def chudnovsky(x):
    pi = Decimal(0)
    a = 0
    while a < x:
        pi += (Decimal(-1)**a) * (Decimal(factorial(6 * a)) / ((factorial(a)**3) * (factorial(3 * a))) * (13591409 + 545140134 * a) / (640320**(3 * a)))
        a += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi**(-1)
    return pi

x = int(input())
getcontext().prec = x+1
print(chudnovsky(x))
