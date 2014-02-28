# This program implements a solution for the 25th Project Euler problem

# NOT COMPLETE
import math

def pow(n, exp):
    result = 1
    for i in range(exp):
        result *= n
    return result

def fib(n):
    nom = round(pow((1+sqFive), n) - pow((1-sqFive), n))
    dNom = round(math.pow(2, n)*sqFive)
    return round(nom/dNom)
# input = int(raw_input("Enter a number: "))
sqFive = math.sqrt(5)
length = 0
print fib(700)

#while len<1000:
#    len = len(fib(n))
#    n++
