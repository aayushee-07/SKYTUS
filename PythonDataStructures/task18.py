# reverse key and value in a dictionary 

student = {
    "Aayushee": 88,
    "Riya": 92,
    "Neha": 85
}

reverse = {}

for key, value in student.items():
    reverse[value] = key

print(reverse)