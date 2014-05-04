import unittest
import problem96 as p

class FileReading(unittest.TestCase):

    lines_for_index = ((1, [9,0,0,3,0,5,0,0,1]),
                       (8, [0,0,5,0,1,0,3,0,0]), 
                       (5, [0,0,6,7,0,8,2,0,0]))

    columns_for_index = ((0, [0,9,0,0,7,0,0,8,0]),
                         (8, [0,1,0,0,8,0,0,9,0]))

    tiles_for_index = ((0, [0,0,3,9,0,0,0,0,1]), 
                       (8, [5,0,0,0,0,9,3,0,0]))

    def test_file_read_correctly(self):
        self.assertEqual(p.first_grid, [[0,0,3,0,2,0,6,0,0],
                                        [9,0,0,3,0,5,0,0,1],
                                        [0,0,1,8,0,6,4,0,0],
                                        [0,0,8,1,0,2,9,0,0],
                                        [7,0,0,0,0,0,0,0,8],
                                        [0,0,6,7,0,8,2,0,0],
                                        [0,0,2,6,0,9,5,0,0],
                                        [8,0,0,2,0,3,0,0,9],
                                        [0,0,5,0,1,0,3,0,0]])

    def test_line_at_index(self):
        for index, line in self.lines_for_index:
            test_line = p.line_at_index(index)
            self.assertEqual(test_line, line)

    def test_columns_at_index(self):
        for index, column in self.columns_for_index:
            test_column = p.column_at_index(index)
            self.assertEqual(test_column, column)

    def test_tile_at_index(self):
        for index, tile in self.tiles_for_index:
            test_tile = p.tile_at_index(index)
            self.assertEqual(test_tile, tile)

    def test_tile_index(self):
        self.assertEqual(p.tile_index(0, 0), 0)
        self.assertEqual(p.tile_index(8, 8), 8)
        self.assertEqual(p.tile_index(3, 0), 3)

class Solving(unittest.TestCase):

    def test_if_solved(self):
        solved_grid = p.solve()
        self.assertEqual(solved_grid, ['483921657', 
                                       '967345821',
                                       '251876493',
                                       '548132976',
                                       '729564138',
                                       '136798245',
                                       '372689514',
                                       '814253769',
                                       '695417382'])


if __name__ == '__main__':
    unittest.main()

