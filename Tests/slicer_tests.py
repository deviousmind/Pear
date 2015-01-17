import unittest
from Cutlery.slicer import Slicer

class SlicerTests(unittest.TestCase):

    def setUp(self):
        self.Slicer = Slicer()

    def tearDown(self):
        del self.Slicer

    def test_slice_returns_random_number_between_0_and_value(self):
        max_val = 4
        values = self.Slicer.slice(max_val)
        self.assertTrue(0 <= values[0] <= max_val)

    def test_slice_returns_two_different_numbers(self):
        values = self.Slicer.slice(1)
        self.assertTrue(values[0] != values[1])


if __name__ == "__main__":
    unittest.main()