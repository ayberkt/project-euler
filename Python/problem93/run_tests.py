import unittest as ut
import problem93 as p


class Test(ut.TestCase):

    def test_consecutive_seq(self):
        self.assertEqual(p.consecutive_seq(list(range(10))),
                                           list(range(10)))
        self.assertEqual(p.consecutive_seq([1, 2, 3, 12, 13, 15]),
                         [1, 2, 3])

    def test_target_numbers(self):
        targets = p.target_numbers([1, 2, 3, 4])
        self.assertEqual(max(targets), 36)
        self.assertEqual(len(targets), 31)
        self.assertEqual((sorted(targets)[:28]), list(range(1, 29)))


if __name__ == '__main__':
    ut.main()
