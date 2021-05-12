import unittest
from src.customer import Customer
from src.drink import Drink 

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Brian", 300)
        
    def test_customer_has_name(self):
        expected = "Brian"
        actual = self.customer.name 
        self.assertEqual(expected, actual)
    
    def test_customer_has_wallet(self):
        expected = 300
        actual = self.customer.wallet
        self.assertEqual(expected, actual) 
        
    def test_customer_can_buy_drink(self):
        drink = Drink("Martini", 5)
        self.customer.buy_drink(drink)
        self.assertEqual