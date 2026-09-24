# create a rectangle class with method to find area and parameter 

class rectangle:

    def __init__(self,height,width):
        self.height = height
        self.width = width

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        return 2 * (self.height + self.width)

rectangle1 = rectangle(10,5)

print("Area =", rectangle1.area())
print("Perimeter =", rectangle1.perimeter())



