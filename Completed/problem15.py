from math import factorial

def num_routes(n):
    n_factorial = factorial(n)
    grid_factorial = factorial(n * 2)
    return grid_factorial / n_factorial ** 2

print num_routes(20)