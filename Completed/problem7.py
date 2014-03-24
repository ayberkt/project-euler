import math
import datetime


def nextPrime(n):
    if isPrime(n):
        n += 1
    while not isPrime(n):
        sqrtSet = range(2, int(math.sqrt(n)) + 2)
        if n % 2 == 0:
            n += 1
        else:
            n += 2
    return n


def isPrime(n):
    if n == 2:
        return True
    sqrtSet = range(2, int(math.sqrt(n)) + 2)
    for i in sqrtSet:
        if n % i == 0:
            return False
    return True


def nPrime(nTerm):
    n = 2
    for i in range(nTerm - 1):
        n = nextPrime(n)
    print n
timeInit = datetime.datetime.now()
print nPrime(10001)
print datetime.datetime.now() - timeInit
