# write a program to create a custom exeption for invalid age <18 

class InvalidAge(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAge

    print("You are eligible for voting")

except InvalidAge:
    print("You are not eligible for voting")

except ValueError:
    print("Please enter a valid number!")

