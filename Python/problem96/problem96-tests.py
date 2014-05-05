import unittest
import problem96 as p

class FileReading(unittest.TestCase):

    initial_grid = [[0,0,3,0,2,0,6,0,0],
                    [9,0,0,3,0,5,0,0,1],
                    [0,0,1,8,0,6,4,0,0],
                    [0,0,8,1,0,2,9,0,0],
                    [7,0,0,0,0,0,0,0,8],
                    [0,0,6,7,0,8,2,0,0],
                    [0,0,2,6,0,9,5,0,0],
                    [8,0,0,2,0,3,0,0,9],
                    [0,0,5,0,1,0,3,0,0]]

    lines_for_index = ((1, [9,0,0,3,0,5,0,0,1]),
                       (8, [0,0,5,0,1,0,3,0,0]), 
                       (5, [0,0,6,7,0,8,2,0,0]))

    columns_for_index = ((0, [0,9,0,0,7,0,0,8,0]),
                         (8, [0,1,0,0,8,0,0,9,0]))

    tiles_for_index = ((0, [0,0,3,9,0,0,0,0,1]), 
                       (8, [5,0,0,0,0,9,3,0,0]))

    def test_file_read_correctly(self):
        self.assertEqual(p.first_grid, self.initial_grid)

    def test_grid_at_index(self):
        self.assertEqual(p.grid_at_index(0), self.initial_grid)
        self.assertEqual(p.grid_at_index(1), [[2,0,0,0,8,0,3,0,0],
                                                   [0,6,0,0,7,0,0,8,4],
                                                   [0,3,0,5,0,0,2,0,9],
                                                   [0,0,0,1,0,5,4,0,8],
                                                   [0,0,0,0,0,0,0,0,0],
                                                   [4,0,2,7,0,6,0,0,0],
                                                   [3,0,1,0,0,7,0,4,0],
                                                   [7,2,0,0,4,0,0,6,0],
                                                   [0,0,4,0,1,0,0,0,3]])

    def test_line_at_index(self):
        for index, line in self.lines_for_index:
            test_line = p.line_at_index(index, self.initial_grid)
            self.assertEqual(test_line, line)

    def test_columns_at_index(self):
        for index, column in self.columns_for_index:
            test_column = p.column_at_index(index, self.initial_grid)
            self.assertEqual(test_column, column)

    def test_tile_at_index(self):
        for index, tile in self.tiles_for_index:
            test_tile = p.tile_at_index(index, self.initial_grid)
            self.assertEqual(test_tile, tile)

    def test_tile_index(self):
        self.assertEqual(p.tile_index(0, 0), 0)
        self.assertEqual(p.tile_index(8, 8), 8)
        self.assertEqual(p.tile_index(3, 0), 3)

class Solving(unittest.TestCase):

    initial_grid = [[0,0,3,0,2,0,6,0,0],
                    [9,0,0,3,0,5,0,0,1],
                    [0,0,1,8,0,6,4,0,0],
                    [0,0,8,1,0,2,9,0,0],
                    [7,0,0,0,0,0,0,0,8],
                    [0,0,6,7,0,8,2,0,0],
                    [0,0,2,6,0,9,5,0,0],
                    [8,0,0,2,0,3,0,0,9],
                    [0,0,5,0,1,0,3,0,0]]

    solved_grid = [[4,8,3,9,2,1,6,5,7], 
                   [9,6,7,3,4,5,8,2,1],
                   [2,5,1,8,7,6,4,9,3],
                   [5,4,8,1,3,2,9,7,6],
                   [7,2,9,5,6,4,1,3,8],
                   [1,3,6,7,9,8,2,4,5],
                   [3,7,2,6,8,9,5,1,4],
                   [8,1,4,2,5,3,7,6,9],
                   [6,9,5,4,1,7,3,8,2]] 

    def test_line_valid(self):
        self.assertEqual(p.line_valid(self.solved_grid[0], 0, self.initial_grid), True)
        self.assertEqual(p.line_valid([1] * 9, 1, self.initial_grid), False) 

    def test_if_solved(self):
        solved_grid = p.solve(self.initial_grid)
        self.assertEqual(solved_grid, [[4,8,3,9,2,1,6,5,7], 
                                       [9,6,7,3,4,5,8,2,1],
                                       [2,5,1,8,7,6,4,9,3],
                                       [5,4,8,1,3,2,9,7,6],
                                       [7,2,9,5,6,4,1,3,8],
                                       [1,3,6,7,9,8,2,4,5],
                                       [3,7,2,6,8,9,5,1,4],
                                       [8,1,4,2,5,3,7,6,9],
                                       [6,9,5,4,1,7,3,8,2]])


if __name__ == '__main__':
    unittest.main()

