import unittest

from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Lion", 1000)
        self.drink_1 = Drink("Martini", 5)
        self.drink_2 = Drink("Rusty Nail", 6)
        self.drink_3 = Drink("Pinot Grigio", 7)
        self.drinks = [self.drink_1, self.drink_2, self.drink_3]

    def test_pub_has_name(self):
        expected = "The Lion"
        actual = self.pub.name
        self.assertEqual(expected, actual)
   
    def test_pub_has_till(self):
        expected = 1000
        actual = self.pub.till         
        self.assertEqual(expected, actual)
        
    def test_has_drinks(self):
        expected = [self.drink_1, self.drink_2, self.drink_3]
        actual = self.drinks
        self.assertEqual(expected, actual)
        

    
    