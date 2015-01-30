import unittest
from Cutlery.spatula import Spatula
from FirstAid.not_a_pair_error import NotAPairError
from unittest.mock import Mock


class SpatulaTests(unittest.TestCase):

    def setUp(self):
        self.Spatula = Spatula()

    def tearDown(self):
        del self.Spatula

    def test_get_people_extracts_list_from_space_separated_string(self):
        people = self.Spatula.get_people("one two three")
        self.assertEqual(people, ['one', 'two', 'three'])

    def test_get_people_extracts_list_from_any_separated_string(self):
        people = self.Spatula.get_people("one, two& three (four)five")
        self.assertEqual(people, ['one', 'two', 'three', 'four', 'five'])

    def test_get_pair_extracts_pair_from_space_separated_string(self):
        pair = self.Spatula.get_pair("[one, two]")
        self.assertEqual(pair, ['one', 'two'])

    def test_get_pair_extracts_pair_from_any_separated_string(self):
        pair = self.Spatula.get_pair("[one two]")
        self.assertEqual(pair, ['one', 'two'])

    def test_get_pair_returns_empty_list_if_string_does_not_contain_people(self):
        pairs = self.Spatula.get_pair('[]')
        self.assertEqual(pairs, [])

    def test_get_pairs_returns_empty_list_if_string_is_empty(self):
        pairs = self.Spatula.get_pairs('')
        self.assertEqual(pairs, [])

    def test_get_pairs_returns_empty_list_if_string_does_not_contain_people(self):
        pairs = self.Spatula.get_pairs('[]')
        self.assertEqual(pairs, [])

    def test_get_pairs_composes_pair_list(self):
        pairs = self.Spatula.get_pairs("[one, two] [three, four]")
        self.assertEqual(pairs, [['one', 'two'], ['three', 'four']])

    def test_get_pairs_composes_any_separated_pair_list(self):
        pairs = self.Spatula.get_pairs("[one two], [three four] [five six]&[seven, eight]")
        self.assertEqual(pairs, [['one', 'two'], ['three', 'four'], ['five', 'six'], ['seven', 'eight']])

    def test_get_pairs_throws_error_if_no_brackets_found(self):
        self.assertRaises(NotAPairError, self.Spatula.get_pairs, "me you")

    def test_remove_people_gets_people_from_raw_text(self):
        self.Spatula.get_people = Mock(return_value=[])
        expected = "one two"
        self.Spatula.remove_people([], expected)

        self.Spatula.get_people.assert_called_with(expected)

    def test_remove_people_removes_people_from_list(self):
        missing_people = ["me", "myself"]
        self.Spatula.get_people = Mock(return_value=missing_people)
        result = self.Spatula.remove_people(["me", "myself", "i"], "me myself")

        self.assertEqual(result, ["i"])

    def test_remove_people_removes_people_ignoring_case(self):
        missing_people = ["mE", "mYseLf"]
        self.Spatula.get_people = Mock(return_value=missing_people)
        result = self.Spatula.remove_people(["me", "myself", "i"], "mE mYseLf")

        self.assertEqual(result, ["i"])

if __name__ == '__main__':
    unittest.main()