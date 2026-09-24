# create a class with private attributes getter and setter methods 

class Student:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


s1 = Student("Aayushee")

print("Name:", s1.get_name())

s1.set_name("Riya")

print("New name:", s1.get_name())