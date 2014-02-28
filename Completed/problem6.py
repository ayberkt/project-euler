''' This program implements a solution for the 6th project euler problem.
The aim is to find the difference between the sum of squares and the square
of the sum. This program takes advantage of a rally simple logic. The sum of
integers up to n is (n(n+1))/2 if we square this we get (n^4+2n^3+n^2)/2 thus
this is the square of sum of integers up to n. Similarly, the sum of squares of
integers is determined by the formula (n(n+1)(2n+1))/6. '''

import math

def squareOfSum(n):
    return math.pow((n*n+n)/2, 2)

def sumOfSquares(n):
    return (n*(n+1)*(2*n+1))/6

while True:
    upperLimit = int(raw_input("Please enter the limit: "))
    print squareOfSum(upperLimit) - sumOfSquares(upperLimit)
