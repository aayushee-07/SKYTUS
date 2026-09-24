# create a Teacher and student class to show inheritance 

class Person:

    def show_name(self):
        print("My name is Aayushee")

class Teacher(Person):

    def teach(self):
        print("Teacher is teaching")

class Student(Person):

    def study(self):
        print("Student is studying")

t1 = Teacher()
s1 = Student()

t1.show_name()
t1.teach()

s1.show_name()
s1.study()