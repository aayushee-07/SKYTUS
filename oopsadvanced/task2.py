# create a  class hereirchy for vehicle --> car --> electricalcar

class Vehicle:

    def brake(self):
        print("Vehicle is braking")


class Car(Vehicle):

    def brake(self):
        print("Car is braking")


class ElectricCar(Car):

    def brake(self):
        print("Electric car is braking")

v1= Vehicle()
c1= Car()
e1= ElectricCar()

v1.brake()
c1.brake()
e1.brake()


