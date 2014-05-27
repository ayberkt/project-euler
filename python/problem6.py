from math import pow

def square_of_sum(n): return pow((n * n + n) / 2, 2)

def sum_of_squares(n): return (n * (n + 1) * (2 * n + 1)) / 6

print(square_of_sum(100) - sum_of_squares(100))
