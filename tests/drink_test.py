import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Martini", 5, 4)
        
    def test_drink_has_name(self,):
        expected = "Martini"
        actual = self.drink.name
        self.assertEqual(expected, actual)

    def test_drink_has_price(self):
        expected = 5
        actual = self.drink.price
        self.assertEqual(expected, actual)

    
    def test_drink_has_alcohol_level(self):
        expected = 4
        actual = self.drink.alcohol_level
        self.assertEqual(expected, actual)