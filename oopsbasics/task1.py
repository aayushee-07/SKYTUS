# create class car with attribute like brand model and speed to method to accelertae/brake 

class Car:
    def __init__(self,brand,model,speed):
         self.brand = brand 
         self.model = model
         self.speed = speed

    def accelerate(self):
         self.speed += 10
         print("speed incresed to:",self.speed)

    def brake(self):
         self.speed -=10
         print("speed decreased to:", self.speed)


car1 = Car("Toyota","Fortuner",50)

print("Brand:",car1.brand)
print("Model:",car1.model)
print("Speed:",car1.speed)

car1.accelerate()
car1.brake()
