import math
import datetime


def build_sieve(limit):
    factors = [2] + (3, limit + 1, 2):

    # Removes the multiples of all numbers up to limit.
    for j in range(3, int(math.sqrt(limit + 1))):
        for q in factors:
            if q % j == 0 and q != j:
                factors.remove(q)
    return factors

while True:
    number = int(raw_input("Please input a number: "))
    # Passes the sqrt of the number as the limit for sieve building.
    sieve = buildSieve(int(math.sqrt(number)) + 1)

    i = 0
    while number > 1:
        try:
            if number % sieve[i] == 0:
                number = number / sieve[i]
                print sieve[i]
                print number
            else:
                i += 1
        except IndexError:
            print "The number is prime."
            break
