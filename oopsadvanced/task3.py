# implement method overriding in a base and derived class 

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


a1 = Animal()
d1 = Dog()

a1.sound()
d1.sound()