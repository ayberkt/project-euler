import math
import datetime

def buildSieve(limit):
    factors = [2]

    for i in range (3, limit+1, 2): factors.append(i) #Creates the base of sieve. Basically an array with all odd numbers up to limit.

    for j in range (3, int(math.sqrt(limit+1))): # Removes the multiples of all numbers up to limit.
        for q in factors:
            if q % j == 0 and q != j:
                factors.remove(q)
    return factors

while True:
    number = int(raw_input("Please input a number: "))
    sieve = buildSieve(int(math.sqrt(number))+1) # Passes the sqrt of the number as the limit for sieve building.
    
    
    i = 0
    while number > 1:
        try:
            if number % sieve[i] == 0:
                number = number/sieve[i]
                print sieve[i]
                print number
            else:
                i += 1
        except IndexError:
            print "The number is prime."
            break

