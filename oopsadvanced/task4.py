# demonstate multiple inheritance with two parent class 

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Bird:

    def fly(self):
        print("Bird can fly")


class Bat(Animal, Bird):
    pass


bat1 = Bat()

bat1.sound()
bat1.fly()