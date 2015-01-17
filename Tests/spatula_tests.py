import unittest
from Cutlery.spatula import Spatula

class SpatulaTests(unittest.TestCase):

    def setUp(self):
        self.Spatula = Spatula()

    def tearDown(self):
        del self.Spatula

    def test_get_people_extracts_list_from_space_separated_string(self):
        people = self.Spatula.get_people("one two three")
        self.assertEqual(people, ['one', 'two', 'three'])

    def test_get_pair_extracts_pair_from_space_separated_string(self):
        pair = self.Spatula.get_pair("[one, two]")
        self.assertEqual(pair, ['one', 'two'])

    def test_get_pairs_returns_empty_list_if_string_is_empty(self):
        pairs = self.Spatula.get_pairs('')
        self.assertEqual(pairs, [])

    def test_get_pairs_composes_pair_list(self):
        pairs = self.Spatula.get_pairs("[one, two] [three, four]")
        self.assertEqual(pairs, [['one', 'two'], ['three', 'four']])

if __name__ == '__main__':
    unittest.main()