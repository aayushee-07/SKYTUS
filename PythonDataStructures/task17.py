# find key with the maximum value in a dictionary 

marks = {
    "Aayushee": 88,
    "Riya": 92,
    "Neha": 85
}

highest = max(marks, key=marks.get)

print("Key with maximum value:", highest)