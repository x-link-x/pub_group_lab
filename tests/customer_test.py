import unittest
from src.customer import Customer
from src.drink import Drink 

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Brian", 300, 28)
        self.drink = Drink("Martini", 5, 4) 
    
    def test_customer_has_name(self):
        expected = "Brian"
        actual = self.customer.name 
        self.assertEqual(expected, actual)
    
    def test_customer_has_wallet(self):
        expected = 300
        actual = self.customer.wallet
        self.assertEqual(expected, actual) 
        
    def test_customer_can_buy_drink(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(295, self.customer.wallet)
        
    def test_customer_has_age(self):
        self.assertEqual(28, self.customer.age)

    def test_customer_drunkenness_goes_up_by_drink(self):
        expected = 4
        self.customer.buy_drink(self.drink)
        actual = self.customer.drunkenness
        self.assertEqual(expected, actual)
