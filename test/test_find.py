import unittest
from _.main import find


class Sut(unittest.TestCase):

    def setUp(self):
        self.sut = find

    def test_find_returns_first_element_that_satisfies_predicate(self):
        first = {"id": 1, "size": "L"}
        second = {"id": 2, "size": "M"}
        third = {"id": 3, "size": "M"}
        expected = second
        actual = self.sut([first, second, third], lambda e: e["size"] == "M")
        self.assertEqual(expected, actual)
