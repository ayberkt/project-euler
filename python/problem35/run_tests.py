import unittest
import problem35 as p


class Test(unittest.TestCase):

    rotations_197 = [197, 971, 719]

    def test_rotations(self):
        self.assertEqual(set(p.rotations(197)), set(self.rotations_197))


if __name__ == '__main__':
    unittest.main()
