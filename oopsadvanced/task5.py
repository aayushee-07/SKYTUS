# create a polymorphic function thatworks with different shapes.

class Circle:

    def area(self):
        return 3.14 * 5 * 5

class Rectangle:

    def area(self):
        return 10 * 5

def show_area(shape):
    print("Area =", shape.area())


c1 = Circle()
r1 = Rectangle()

show_area(c1)
show_area(r1)