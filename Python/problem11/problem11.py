from operator import mul
from functools import reduce

def column_at_index(index, grid): return [line[index] for line in grid]

def diagonal_at_index(line_index, column_index, grid):
    diagonal = []
    while True:
        try:
            diagonal.append(grid[line_index][column_index])
        except IndexError:
            return diagonal
        line_index += 1
        column_index += 1

def max_sum_consecutive(num_list):
    greatest = 0
    for i in range(len(num_list) - 3):
        product = reduce(mul, [num_list[j] for j in range(i, i+4)])
        if product > greatest: greatest = product
    return greatest

number_grid = open('grid.txt').readlines()
grid = [[int(num) for num in line.split(' ')] for line in number_grid]

greatest = 0

for line in grid:
    max_product = max_sum_consecutive(line)
    if max_product > greatest: greatest = max_product

for column in [column_at_index(index, grid) for index in range(20)]:
    max_product = max_sum_consecutive(column)
    if max_product > greatest: greatest = max_product

for diagonal in [diagonal_at_index(index, 0, grid) for index in range(20)]:
    max_product = max_sum_consecutive(diagonal)
    if max_product > greatest: greatest = max_product

for diagonal in [diagonal_at_index(0, index, grid) for index in range(20)]:
    max_product = max_sum_consecutive(diagonal)
    print(diagonal)
    if max_product > greatest: greatest = max_product

grid = [line[::-1] for line in grid]

for diagonal in [diagonal_at_index(index, 0, grid) for index in range(20)]:
    max_product = max_sum_consecutive(diagonal)
    if max_product > greatest: greatest = max_product

for diagonal in [diagonal_at_index(0, index, grid) for index in range(20)]:
    max_product = max_sum_consecutive(diagonal)
    print(diagonal)
    if max_product > greatest: greatest = max_product



print(greatest)
