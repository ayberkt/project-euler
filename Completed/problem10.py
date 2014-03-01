import math

def build_sieve(limit):

    factors = [2]

    for i in range (3, limit, 2): factors.append(i) #Creates the base of sieve.

    for j in range (3, int(math.sqrt(limit+1))): # Removes the multiples of all numbers up to limit.
        for q in factors:
            if q % j == 0 and q != j:
                factors.remove(q)
    return factors

while True:
    number = int(raw_input("Please input a number: "))
    sieve = build_sieve(number) # Passes the sqrt of the number as the limit for sieve building.
    print (sum(sieve))
