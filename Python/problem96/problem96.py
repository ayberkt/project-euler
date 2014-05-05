from itertools import permutations

grids_file = open('sudoku.txt')

first_grid = [list(line.strip()) for line in grids_file if 'Grid' not in line][0:9]

for j in range(len(first_grid)):
    new_line = []
    for num_str in first_grid[j]:
        new_line.append(int(num_str))
    first_grid[j] = new_line

# [print(line, end='\n') for line in first_grid]

def grid_at_index(index):
    with open('sudoku.txt') as grids_file:
        init_grid = [list(line.strip()) for line in grids_file if 'Grid' not in line][(index * 9):9 + (index * 9)]

        for j in range(len(init_grid)):
            new_line = []
            for num_str in init_grid[j]:
                new_line.append(int(num_str))
            init_grid[j] = new_line
        
        return init_grid

def line_at_index(index, grid): return grid[index]

def column_at_index(index, grid): return [line[index] for line in grid]

def tile_at_index(index, grid):
    if index == 0 or index == 1 or index == 2:
        lines = (0, 1, 2)
    elif index == 3 or index == 4 or index == 5:
        lines = (3, 4, 5)
    elif index == 6 or index == 7 or index == 8:
        lines = (6, 7, 8)
    
    columns = [i + (index % 3) * 3 for i in (0, 1, 2)]

    tile = []
    for line in lines:
        for column in columns:
            tile.append(grid[line][column])
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

def solve(grid):
    while True:
        [print(line, end='\n\n') for line in grid]
        print('\n* * * * * \n')
        for line_index in range(9):
            for col_index in range(9):
                if grid[line_index][col_index] == 0:
                    possibilites = set([i for i in range(1, 10)])

                    possibilites.difference_update(set(grid[line_index]))

                    possibilites.difference_update(set(column_at_index(col_index, grid)))

                    possibilites.difference_update(set(tile_at_index(tile_index(line_index, col_index), grid)))

                    if len(possibilites) == 1:
                        print(possibilites, grid[line_index], grid[line_index][col_index])
                        new_line = list(grid[line_index])
                        new_line[col_index] = list(possibilites)[0]
                        grid[line_index] = new_line

        if sum([sum(line) for line in grid]) == 45 * 9:
            return grid

def line_valid(line_candidate, line_index, grid):
    for cell_index in range(len(line_candidate)):
        if grid[line_index][cell_index] != 0 and grid[line_index][cell_index] == line_candidate[cell_index]:
            print("Returning false since {0} is not equal to {1}".format(line_candidate[cell_index], grid[line_index][cell_index]))
            return False
        if line_candidate[cell_index] in set(tile_at_index(tile_index(line_index, cell_index), grid)):
            return False
        if line_candidate[cell_index] in set(column_at_index(cell_index, grid)):
            return False

    return True


if __name__ == "__main__":
    # current_grid = grid_at_index(i)
    
    [line for line in permutations(range(1, 10)) if line_valid(line)]
