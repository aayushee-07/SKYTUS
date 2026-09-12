# merge two dictonary into one

student1 = {
    "name": "Aayushee",
    "age": 20
}

student2 = {
    "marks": 88,
    "city": "Gujarat"
}

student = student1 | student2

print(student)