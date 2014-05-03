grids_file = open('sudoku.txt')

first_grid = [line.strip() for line in grids_file if 'Grid' not in line][0:9]

def line_at_index(index): return first_grid[index]

def column_at_index(index): return ''.join([str(line[index]) for line in first_grid])

def tile_at_index(index):
    if index == 0 or index == 1 or index == 2:
        lines = (0, 1, 2)
    elif index == 3 or index == 4 or index == 5:
        lines = (3, 4, 5)
    elif index == 6 or index == 7 or index == 8:
        lines = (6, 7, 8)
    
    columns = [i + (index % 3) * 3 for i in (0, 1, 2)]

    tile = ''
    for line in lines:
        for column in columns:
            tile += first_grid[line][column]
    return tile

def tile_index(line_index, col_index):
    tile_index = 0

    if line_index < 3:
        tile_index = 0
    elif 3 <= line_index < 6:
        tile_index = 3
    elif 6 <= line_index:
        tile_index = 6

    if col_index < 3:
        tile_index += 0
    elif 3 <= col_index < 6:
        tile_index += 1
    elif 6 <= col_index:
        tile_index += 2

    return tile_index


def solve():
    while True:
        for line_index in range(9):
            print(first_grid)
            for col_index in range(9):
                possibilites = set([str(i) for i in range(1, 10)])
                possibilites.difference_update(set([i for i in line_at_index(line_index) if i != '0']))
                possibilites.difference_update(set([i for i in column_at_index(col_index) if i != '0']))
                possibilites.difference_update(set([i for i in tile_at_index(tile_index(line_index, col_index)) if i != '0']))

                if len(possibilites) == 1:
                    new_line = list(first_grid[line_index])
                    new_line[col_index] = list(possibilites)[0]
                    first_grid[line_index] = ''.join(new_line)

        if not len([line for line in first_grid if '0' in line]):
            return first_grid

if __name__ == "__main__":
    solve()