from itertools import permutations

def is_prime(n):
    if n == 2:
        return True
    sqrtSet = range(2, int(n ** 0.5) + 2)
    for i in sqrtSet:
        if n % i == 0:
            return False
    return True

def is_circular_prime(n):
    for num in [int(''.join(digits)) for digits in permutations(str(n))]:
        if not is_prime(num):
            return False
    return True

def rotations(num):
    num_str = str(num)

primes = [num for num in range(2, 1000000) if is_prime(num)]
print([num for num in range(2, 1000000) if is_circular_prime(num)])
