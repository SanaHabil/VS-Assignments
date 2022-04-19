#import the store.py file.
import store    

class Product:
    def __init__(self, name, price, category,pid):
        self.name = name
        self.price = price
        self.category = category
        self.pid = pid

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += percent_change
        else:
            self.price -= percent_change
        return self

    def print_info(self):
        print(f"Product Name: {self.name}", f"Price:{self.price}", f" Category: {self.category}")
        return self
        
