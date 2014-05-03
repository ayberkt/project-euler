import unittest
import problem96 as p

class FileReading(unittest.TestCase):

    lines_for_index = ((1, '900305001'),
                       (8, '005010300'), 
                       (5, '006708200'))

    columns_for_index = ((0, '090070080'),
                         (8, '010080090'))

    tiles_for_index = ((0, '003900001'), 
                       (8, '500009300'))

    def test_file_read_correctly(self):
        self.assertEqual(p.first_grid, ['003020600',
                                       '900305001',
                                       '001806400',
                                       '008102900',
                                       '700000008',
                                       '006708200',
                                       '002609500',
                                       '800203009',
                                       '005010300'])

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

    def test_solve(self):
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
