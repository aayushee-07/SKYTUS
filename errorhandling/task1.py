# write a program to handle divison by zero error

num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))

try:
    result = num1 / num2
    print("Result: ",result)

except ZeroDivisionError:
    print("can not divide by zero: ")

    