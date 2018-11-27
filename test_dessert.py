from unittest import TestCase
from desserts import Dessert


class DessertTests(TestCase):
    def setUp(self):
        self.dessert = Dessert(1, "Snickerdoodle cookies", "Best name ever",
                               200)

    def test_init(self):
        """Test the __init__ method for Dessert"""

        pass

    def test_repr(self):
        """Test the __repr__ method for Dessert"""

        pass

    def test_serialize(self):
        """Test the serialize method for Dessert"""

        pass
