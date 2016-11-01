import unittest
from _ import find_index

class sut(unittest.TestCase):

    def setUp(self):

        self.find_index = find_index.find_index

    def test_find_index_returns_index_of_first_element_that_satisfies_predicate(self):
        first = {"id": 1, "size": "L"}
        second = {"id": 2, "size": "M"}
        third = {"id": 3, "size": "M"}
        expected = 1
        actual = self.find_index([first, second, third], lambda e: e["size"] == "M")
        self.assertEqual(expected, actual)