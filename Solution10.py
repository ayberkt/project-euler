# This program implements a solution for the 3rd problem of Project Euler

import math
import datetime

def buildSieve(limit):

    timeInitial = datetime.datetime.now()

    factors = [2]

    for i in range (3, limit, 2): factors.append(i) #Creates the base of sieve.

    for j in range (3, int(math.sqrt(limit+1))): # Removes the multiples of all numbers up to limit.
        for q in factors:
            if q % j == 0 and q != j:
                factors.remove(q)
    timeDelta = datetime.datetime.now() - timeInitial
    print("It took " + str(timeDelta) + " for the sieve.")
    return factors

while True:
    number = int(raw_input("Please input a number: "))
    sieve = buildSieve(number) # Passes the sqrt of the number as the limit for sieve building.
    print (sum(sieve))
