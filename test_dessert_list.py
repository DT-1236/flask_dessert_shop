from unittest import TestCase
from desserts import Dessert, DessertList


class BaseDessertListTests(TestCase):
    def setUp(self):
        self.sample_list = DessertList()

    def test_init(self):
        """Test the __init__ method for DessertList"""
        self.assertIsInstance(self.sample_list, DessertList)
        self.assertEqual(self.sample_list.next_id, 1)
        self.assertEqual(self.sample_list.desserts, [])

    def test_repr(self):
        """Test the __repr__ method for DessertList"""
        self.assertEqual(repr(self.sample_list), "nextid = 1\n")


class SingleDessertListTests(TestCase):
    def setUp(self):
        self.sample_list = DessertList()
        self.sample_list.add(
            name='Chocolate Cake',
            description='Made of CHOCOLATE',
            calories=1200)

    def test_add(self):
        """Test the add method for DessertList"""
        self.assertEqual(self.sample_list.next_id, 2)
        self.assertIsInstance(self.sample_list.desserts, list)
        self.assertIsInstance(self.sample_list.desserts[0], Dessert)

    def test_serialize(self):
        """Test the serialize method for DessertList"""
        self.assertIsInstance(self.sample_list.serialize(), list)
        self.assertEqual(self.sample_list.serialize(),
                         [{
                             "id": 1,
                             "name": "Chocolate Cake",
                             "description": "Made of CHOCOLATE",
                             "calories": 1200
                         }])
