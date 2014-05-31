import unittest
import problem35 as p


class Test(unittest.TestCase):

    rotations_197 = [197, 971, 719]

    def test_rotations(self):
        self.assertEqual(set(p.rotations(197)), set(self.rotations_197))
        self.assertEqual(set(p.rotations(123)), set([123, 312, 231]))

    def test_rotational_prime(self):
        self.assertTrue(p.rotational_prime(197))


if __name__ == '__main__':
    unittest.main()
