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

if __name__ == '__main__':
    unittest.main()

