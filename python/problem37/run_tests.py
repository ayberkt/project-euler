import unittest
import problem37 as p


class Test(unittest.TestCase):

    truncatable_primes = [23, 37, 53, 73, 313, 317, 373, 797]

    def test_truncations(self):
        self.assertEqual(set(p.truncations('123')), set(['12', '1',
                                                         '23', '3']))
        self.assertEqual(set(p.truncations('451')), set(['51', '1',
                                                         '45', '4']))
        self.assertEqual(set(p.truncations('3797')), set(['797', '97', '7',
                                                         '379', '37', '3']))

    def test_truncatable_prime(self):
        self.assertTrue(all([p.truncatable_prime(num)
                             for num in self.truncatable_primes]))
        for num in range(13, 1000):
            if num not in self.truncatable_primes:
                self.assertFalse(p.truncatable_prime(num))


if __name__ == '__main__':
    unittest.main()
