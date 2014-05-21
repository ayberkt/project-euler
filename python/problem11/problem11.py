from operator import mul; from functools import reduce

def column_at_index(index, grid): return [line[index] for line in grid]

def diagonal_at_index(line_index, column_index, grid):
    diagonal = []
    while True:
        try:
            diagonal.append(grid[line_index][column_index])
        except IndexError:
            return diagonal
        line_index += 1; column_index += 1

def max_sum_consecutive(num_list):
    greatest = 0
    for i in range(len(num_list) - 3):
        product = reduce(mul, [num_list[j] for j in range(i, i+4)])
        if product > greatest: greatest = product
    return greatest

number_grid = open('grid.txt').readlines()
grid = [[int(num) for num in line.split(' ')] for line in number_grid]
reversed_grid = [line[::-1] for line in grid]

greatest = 0
for index in range(20):
    max_product = max(max_sum_consecutive(grid[index]),
                      max_sum_consecutive(column_at_index(index, grid)),
                      max_sum_consecutive(diagonal_at_index(index, 0, grid)),
                      max_sum_consecutive(diagonal_at_index(0, index, grid)),
                      max_sum_consecutive(diagonal_at_index(0, index, reversed_grid)),
                      max_sum_consecutive(diagonal_at_index(index, 0, reversed_grid)))
    if max_product > greatest: greatest = max_product
print(greatest)
