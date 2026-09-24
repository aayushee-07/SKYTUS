# create a laptop class with a method to apply discount on price 

class Laptop:

    def __init__(self,originalprice,discount):
        self.originalprice= originalprice
        self.discount_percent = discount

    def discount(self):
        return (self.originalprice * self.discount_percent)/100

l1 = Laptop(80000,20)

print("Discount is:",l1.discount())

final_price = l1.originalprice - l1.discount()
print("Final price:", final_price)