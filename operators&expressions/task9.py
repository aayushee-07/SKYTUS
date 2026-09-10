# write program to that uses and & or operator to check multiple conditions 

age = int(input("Enter your age: "))

if age >= 18 and age <= 60:
    print("You are eligible")

if age < 18 or age > 60:
    print("You are not eligible")