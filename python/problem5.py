from functools import reduce
from fractions import gcd


def lcm(a, b):
    return a * b // gcd(a, b)

print(reduce(lcm, range(1, 21)))
