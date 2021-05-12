class Pub:
    
    def __init__(self,name,till):
        self.name = name
        self.till = till 
        self.drinks = []
        

    def customer_is_old_enough(self, customer):
        return customer.age >= 18
    
    def customer_too_drunk(self, customer):
        return customer.drunkenness >= 30

    def serve_drink(self, drink, customer):
        if self.customer_is_old_enough(customer) and not self.customer_too_drunk(customer):
            customer.buy_drink(drink)
            self.till += drink.price
      
        
 
        


    