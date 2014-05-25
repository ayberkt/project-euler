import unittest
import problem112 as p


class Test(unittest.TestCase):

    def test_number_type(self):
        '''Test cases for all three possibilites from the
        problem description.'''
        self.assertEqual(p.number_type(134468), p.NumberType.increasing)
        self.assertEqual(p.number_type(66420), p.NumberType.decreasing)
        self.assertEqual(p.number_type(155349), p.NumberType.bouncy)

if __name__ == '__main__':
    unittest.main()
