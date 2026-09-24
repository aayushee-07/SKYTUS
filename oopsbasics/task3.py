# create a student class with a method to calculate avg marks

class student:

    def __init__(self, marks,student):
        self.marks = marks
        self.student= student

    def avg(self):
            return sum(self.marks) / len(self.marks)

student1 = student([99,77,88],"Aayushee")

print("Average marks:", student1.avg())
print("Student name:", student1.student)
    