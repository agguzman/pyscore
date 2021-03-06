import unittest
from _.main import take_while


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = take_while

    def test_take_while_returns_all_elements_that_satisfy_predicate(self):
        expected = [2, 4]
        actual = self.sut([1, 2, 3, 4], lambda e: e % 2 is 0)
        self.assertEqual(expected, actual)