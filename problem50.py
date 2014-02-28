from math import sqrt
import time

def nextPrime(n):
    if isPrime(n): n+= 1
    while not isPrime(n):
        if n%2 == 0:
            n += 1
        else:
            n+= 2
    return n

def isPrime(n):
    if n == 2: return True
    sqrtSet = range(2, int(sqrt(n))+2)
    for i in sqrtSet:
        if n%i == 0: return False
    return True

time.clock()
primes = []
total = 0
i = 1

while sum(primes) + nextPrime(i) < 1000000:
    i = nextPrime(i)
    primes.append(i)

total = sum(primes)

for i in primes:
    total -= i
    if isPrime(total):
        break

print total
print time.clock()