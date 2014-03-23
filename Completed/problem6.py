import math

def squareOfSum(n):
    return math.pow((n*n+n)/2, 2)

def sumOfSquares(n):
    return (n*(n+1)*(2*n+1))/6

while True:
    upperLimit = int(raw_input("Please enter the limit: "))
    print squareOfSum(upperLimit) - sumOfSquares(upperLimit)
