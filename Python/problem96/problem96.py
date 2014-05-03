grids_file = open('sudoku.txt')

first_grid = [line.strip() for line in grids_file if 'Grid' not in line][0:9]

def line_at_index(index): return first_grid[index]

def column_at_index(index): return ''.join([str(line[index]) for line in first_grid])

def tile_at_index(index):
    if index == 0 or index == 1 or index == 2:
        lines = (0, 1, 2)
    elif index == 3 or index == 4 or index == 5:
        lines = (3, 4, 5)
    elif index == 7 or index == 8 or index == 9:
        lines = (6, 7, 8)
    
    columns = [i + (index % 3) * 3 for i in (0, 1, 2)]

    tile = ''
    for line in lines:
        for column in columns:
            tile += first_grid[line][column]
    return tile