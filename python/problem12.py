from math import sqrt
from operator import mul
import time


def erat(limit):
    factors = [2] + range(3, limit, 2)  # Creates the base of sieve.

    # Removes the multiples of all numbers up to limit.
    for j in range(3, int(sqrt(limit + 1))):
        for q in factors:
            if q % j == 0 and q != j:
                factors.remove(q)

    return factors


def factors(n):
    global primes
    try:
        primes
    except NameError:
        primes = erat(100)
    factors = []
    for i in primes:
        while n % i == 0:
            n /= i
            factors.append(i)
    return factors


def numDivisors(n):
    facs = factors(n)
    occs = []
    for i in facs:
        occs.append(facs.count(i))
        facs = [j for j in facs if j != i]
    occs = map(lambda x: x + 1, occs)
    return reduce(mul, occs)


def triangle(n):
    return (n * (n + 1)) / 2

if __name__ == "__main__":
    global primes
    primes = erat(10000)
    time.clock()
    i = 10
    while True:
        triNum = triangle(i)
        numDiv = numDivisors(triNum)
        print triNum, numDiv
        if numDiv > 500:
            print triNum
            break
        triNum += i
        i += 1
    print time.clock()
