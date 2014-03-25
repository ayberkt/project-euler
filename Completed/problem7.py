import math


def next_prime(n):
    if is_prime(n):
        n += 1
    while not is_prime(n):
        sqrtSet = range(2, int(math.sqrt(n)) + 2)
        if n % 2 == 0:
            n += 1
        else:
            n += 2
    return n


def is_prime(n):
    if n == 2:
        return True
    sqrtSet = range(2, int(math.sqrt(n)) + 2)
    for i in sqrtSet:
        if n % i == 0:
            return False
    return True


def nth_prime(nTerm):
    n = 2
    for i in range(nTerm - 1):
        n = next_prime(n)
    print n

print nth_prime(10001)
