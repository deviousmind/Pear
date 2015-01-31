import unittest
from unittest.mock import Mock
from KitchenStaff.chef import Chef


class ChefTests(unittest.TestCase):
    class FakeCrust:
        def create(self):
            pass

        def add_toppings(self):
            raise IOError

    def setUp(self):
        self.crust = self.FakeCrust()
        self.chef = Chef(self.crust)

    def tearDown(self):
        del self.chef
        del self.crust

    def test_bake_pie_returns_available_people(self):
        expected = ["me", "myself"]
        self.crust.add_toppings = Mock(return_value=expected)

        people = self.chef.bake_pie()

        self.assertEqual(people, expected)

    def test_bake_pie_returns_creates_new_people_if_retrieval_fails(self):
        expected = ["me", "myself"]
        self.crust.create = Mock(return_value=expected)

        people = self.chef.bake_pie()

        self.assertEqual(people, expected)


if __name__ == "__main__":
    unittest.main()