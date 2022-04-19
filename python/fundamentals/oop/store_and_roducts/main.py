import store
import product

# Test out your classes by creating an instance of the Store and a few instances of the Product class, 
# add those instances to the store instance, and then test out the methods.

the_market = store.Store("The_Market")
tissues = product.Product("tissue", 5, "house_hold")
cleaners = product.Product("cleaners", 6, "house_hold")
printng_paper = product.Product("printing_paper", 10, "office")
snaks= product.Product("snaks", 8, "food")
fruites=product.Product("Fruites", 7, "food")
vegis = product.Product("Vegis ", 10, "food")


the_market.add_product(tissues).add_product(cleaners).add_product(printng_paper).add_product(snaks)
#the_market.sell_product(1)
#print(the_market.inflation(10)[0].print_info())

print(the_market.products[1].print_info())
print(the_market.set_clearance("food", 5))
print(the_market.products[3].print_info())
