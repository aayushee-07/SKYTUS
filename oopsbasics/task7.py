# create a circle class to find area and Circumference

class Circle:

    def __init__(self,radius,pi):
        self.radius = radius
        self.pi= pi 

    def area(self):
        return  self.pi * self.radius * self.radius

    def circumfrence(self):
        return 2 * self.pi * self.radius

c1 = Circle (10,3.14)

print("Area of Circle:", c1.area())
print("Circumference of Circle:",c1.circumfrence())