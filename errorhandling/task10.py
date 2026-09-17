# write a program that validates an email format and raises an exceptions for invalid ones. 

class invalidEmailError(Exception):
    pass

try:
    email= input("Enter your mail: ")

    if "@" not in email or "." not in email:
        raise invalidEmailError("Invalid email format!")

    print("valid email")

except invalidEmailError as e:
    print(e)

