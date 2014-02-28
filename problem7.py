# This program implements a solution for the 7th Project Euler problem

"""
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

import math
import datetime

def nextPrime(n):
    if isPrime(n): n+= 1
    while not isPrime(n):
        sqrtSet = range(2, int(math.sqrt(n))+2)
        if n%2 == 0:
            n += 1
        else:
            n+= 2
    return n

def isPrime(n):
    if n == 2: return True
    sqrtSet = range(2, int(math.sqrt(n))+2)
    for i in sqrtSet:
        if n%i == 0: return False
    return True

def nPrime(nTerm):
    n = 2
    for i in range(nTerm-1):
        n = nextPrime(n)
    print n    
timeInit = datetime.datetime.now()
print nPrime(10001)
print datetime.datetime.now() - timeInit
