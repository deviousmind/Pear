import unittest
from unittest.mock import Mock
from KitchenStaff.chef import Chef


class ChefTests(unittest.TestCase):
    class FakePie:
        def create(self):
            pass

        def add_toppings(self):
            raise IOError

    def setUp(self):
        self.pie = self.FakePie()
        self.chef = Chef(self.pie)

    def tearDown(self):
        del self.chef
        del self.pie

    def test_bake_pie_returns_available_people(self):
        expected = ["me", "myself"]
        self.pie.add_toppings = Mock(return_value=expected)

        people = self.chef.bake_pie()

        self.assertEqual(people, expected)

    def test_bake_pie_returns_creates_new_people_if_retrieval_fails(self):
        expected = ["me", "myself"]
        self.pie.create = Mock(return_value=expected)

        people = self.chef.bake_pie()

        self.assertEqual(people, expected)


if __name__ == "__main__":
    unittest.main()