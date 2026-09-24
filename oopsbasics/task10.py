# create a shop class with a method to add and list product 

class Shop:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Product added successfully")

    def list_products(self):
        print("Products:")
        for product in self.products:
            print(product)


shop1 = Shop()

shop1.add_product("Laptop")
shop1.add_product("Mobile")
shop1.add_product("Headphones")

shop1.list_products()