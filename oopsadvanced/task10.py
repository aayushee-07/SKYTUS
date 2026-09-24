# demonstrate the use of super() in inheritance

class Employee:

    def __init__(self, name):
        self.name = name
        print("Employee:", self.name)


class Programmer(Employee):

    def __init__(self, name):
        super().__init__(name)
        print("Programmer:", self.name)


p1 = Programmer("Aayushee")