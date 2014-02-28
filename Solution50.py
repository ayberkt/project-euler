# This program will eventually implement a solution for the
# 50th Project Euler problem

import math

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

def consecPrimeSums(upTo):
	primeSums = [5]
	prime = 5
	while True:
		newSum = primeSums[-1] + prime
		prime = nextPrime(prime)
		if not newSum > upTo:
			primeSums.append(newSum)
		else:
			return primeSums


# while True:
# 	primeSum = sumConsecPrimes(i)
# 	if primeSum >= 1000000000:
# 		break
# 	primeSums.append(primeSum)
# 	i += 1
# # print primeSums

primeSums = consecPrimeSums(1000)

print primeSums

for i in primeSums:
	if i != primeSums[-1]:
		diff = primeSums[primeSums.index(i)+1] - i
		print diff, isPrime(diff)
	# if isPrime(i):
		# print i, isPrime(i)

# print primeSums





