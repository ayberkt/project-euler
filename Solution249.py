# This script will eventually implement a solution for the 249th Project Euler problem.

from itertools import chain, combinations
import math

def powerSet(iterable):
    '''powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)'''
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

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

def primesUpTo(nTerm):
	primes = []
	n = 2
	for i in range(nTerm-1):
		primes.append(n)
		n = nextPrime(n)
	return primes

primeSet = set(primesUpTo(5000))
print set(powerSet(primeSet))
