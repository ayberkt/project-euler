import math

def build_sieve(limit):

    factors = [2] + range(3, limit, 2)

    for j in range (3, int(math.sqrt(limit+1))): # Removes the multiples of all numbers up to limit.
        for q in factors:
            if q % j == 0 and q != j:
                factors.remove(q)
    return factors

while True:
    sieve = build_sieve(2000000)
    print (sum(sieve))
