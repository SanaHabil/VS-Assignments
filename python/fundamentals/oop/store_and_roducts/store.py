from python.fundamentals.oop.store_and_roducts.product import Product


class Store:
    def __init__(self, name):
        self.name  = name 
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)  
        return self

#Remove the item at index id 
    def sell_product(self, pid):
        for prooduct in products:
            if product.pid == pid:
                self.products.remove(product)
        print(f"Product Name: {product.name}")
# inflation
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self.products    
#set_clearance(self, category, percent_discount) 
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self.products