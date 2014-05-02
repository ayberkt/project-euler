grids_file = open('sudoku.txt')

first_grid = [line.strip() for line in grids_file if 'Grid' not in line][0:9]

# possibilites = set([str(i) for i in range(1, 10)])

def line_at_index(index): return first_grid[index]

def column_at_index(index): return ''.join([str(line[index]) for line in first_grid])

def tile_at_index(index):
    for i in range(0, 7, 3)

    [j for j in range(30) if i <= (j % 9) < i+3])
    tile = ''
    for j in range(6):
        triple = ''.join([num for num in first_grid[]])