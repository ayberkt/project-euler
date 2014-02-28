# This program implements a solution for the 5th Project Euler problem

""" 2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?"""

def gcd(a,b):
    r = a%b
    if r == 0: return b
    return gcd(b, r)

def lcm(a,b):
    return a*b // gcd(a,b)

print reduce(lcm, range(1, 21))
