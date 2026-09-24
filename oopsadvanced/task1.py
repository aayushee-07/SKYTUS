# create a base class animal and subclasses dog and cat 

class Animal:

    def eat(self):
        print("Animal is eating")

class Dog(Animal):

    def eat(self):
        print("Dog is eating")

class Cat(Animal):

    def eat(self):
        print("Cat is eating")


a1 = Animal()
d1 = Dog()
c1 = Cat()

a1.eat()
d1.eat()
c1.eat()

