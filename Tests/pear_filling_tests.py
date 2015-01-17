import unittest
from Filling.pear_filling import PearFilling
from Cutlery.slicer import Slicer
from unittest.mock import Mock

class PearFillingTests(unittest.TestCase):

    def setUp(self):
        self.Slicer = Slicer()
        self.Slicer.slice = Mock(return_value=[0, 1])
        self.Pear = PearFilling(self.Slicer)

    def tearDown(self):
        del self.Pear
        del self.Slicer

    def test_create_pair_gets_random_indexes_up_to_maximum_number_people(self):
        self.Slicer.slice = Mock(return_value=[0, 2])
        number_pairs = ['uno', 'deux', 'three']
        self.Pear.create_pair(number_pairs)
        self.Slicer.slice.assert_called_with(len(number_pairs) - 1)

    def test_create_pair_returns_pair_at_expected_indexes(self):
        self.Slicer.slice = Mock(return_value=[1, 3])
        pair = self.Pear.create_pair(['zero', 'one', 'two', 'three'])
        self.assertEqual(pair, ['one', 'three'])

    def test_create_pairs_returns_pairs_until_none_can_be_made(self):
        pairs = self.Pear.create_pairs(['one', 'one', 'two', 'two'], [])
        self.assertEqual(len(pairs), 2)

    def test_create_pairs_returns_expected_pairs(self):
        self.Slicer.slice = Mock(side_effect=[[1, 3], [0, 1]])
        pairs = self.Pear.create_pairs(['zero', 'one', 'two', 'three'], [])
        self.assertEqual(pairs[0], ['one', 'three'])
        self.assertEqual(pairs[1], ['zero', 'two'])

    def test_create_pairs_returns_single_person_if_not_enough_people_left_for_pair(self):
        self.Slicer.slice = Mock(side_effect=[[0, 2]])
        pairs = self.Pear.create_pairs(['zero', 'solo', 'two'], [])
        self.assertEqual(pairs[1], ['solo'])

    def test_create_pairs_does_not_pair_people_if_they_cannot_pair(self):
        self.Slicer.slice = Mock(side_effect=[[0, 1], [0, 1], [0, 2], [0, 1]])
        pairs = self.Pear.create_pairs(['can', 'not', 'we', 'you'], [['can', 'not']])
        self.assertNotIn(['can', 'not'], pairs)

    def test_create_pairs_does_not_pair_people_in_any_order_if_they_cannot_pair(self):
        self.Slicer.slice = Mock(side_effect=[[1, 0], [0, 1], [0, 2], [0, 1]])
        pairs = self.Pear.create_pairs(['can', 'not', 'we', 'you'], [['can', 'not']])
        self.assertNotIn(['not', 'can'], pairs)

    def test_create_pairs_allows_cannot_pair_to_pair_if_another_pair_is_impossible(self):
        self.Slicer.slice = Mock(side_effect=[[0, 1], [0, 1], [0, 1]])
        pairs = self.Pear.create_pairs(['can', 'not'], [['can', 'not']])
        self.assertEqual(pairs[0], ['can', 'not'])

    def test_create_pairs_returns_empty_list_if_pair_cannot_be_made(self):
        pairs = self.Pear.create_pairs([], [])
        self.assertEqual(pairs, [])




if __name__ == "__main__":
    unittest.main()