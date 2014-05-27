import math

def build_sieve(limit):

    factors = [2] + range(3, limit, 2)

    for j in range (3, int(math.sqrt(limit+1))): # Removes the multiples of all numbers up to limit.
        for q in factors:
            if q % j == 0 and q != j:
                factors.remove(q)
    return factors

while True:
    number = int(raw_input("Please input a number: "))
    sieve = build_sieve(number).
    print (sum(sieve))
