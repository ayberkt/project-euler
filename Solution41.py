# This script will implement a solution for the 41st Project Euler Problem.

import math

def isPandigit(n):
	digits = set(range(1, len(str(n))+1))
	print digits
	digitsOfN = set(map(int, str(n)))
	print digitsOfN
	if digitsOfN == digits:
		return True
	else:
		return False

def isPrime(n):
    if n == 2: return True
    sqrtSet = range(2, int(math.sqrt(n))+2)
    for i in sqrtSet:
        if n%i == 0: return False
    return True

print isPrime(14)