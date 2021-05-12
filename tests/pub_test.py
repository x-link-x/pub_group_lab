import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Lion", 1000)
        self.drink_1 = Drink("Martini", 5, 4)
        self.drink_2 = Drink("Rusty Nail", 6, 10)
        self.drink_3 = Drink("Pinot Grigio", 7, 8)
        self.drinks = [self.drink_1, self.drink_2, self.drink_3]
        self.customer_1 = Customer("Brian", 300, 28)
        self.customer_2 = Customer("Tim", 5, 12)
    

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

    def test_serve_drink_increases_money_in_till(self):
        expected = 1005
        self.pub.serve_drink(self.drink_1, self.customer_1)
        actual = self.pub.till
        self.assertEqual(expected, actual)

    def test_customer_is_old_enough_returns_true(self):
        self.assertEqual(True,self.pub.customer_is_old_enough(self.customer_1))
    
    def test_not_served_if_underage(self):
        self.pub.serve_drink(self.drink_1, self.customer_2)
        expected = 1000
        actual = self.pub.till
        self.assertEqual(expected, actual)

    def test_not_served_too_drunk(self):
        self.pub.serve_drink(self.drink_2, self.customer_1)
        self.pub.serve_drink(self.drink_2, self.customer_1)
        self.pub.serve_drink(self.drink_2, self.customer_1)
        self.pub.serve_drink(self.drink_2, self.customer_1)
        expected = 1018
        actual = self.pub.till
        self.assertEqual(expected, actual)
        
        
        


       
        

    
    