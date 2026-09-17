# write a program to demonstrate multiple exeption blocks 

try:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter thr second number: "))

    result= num1 / num2
    print("You entered: ",result)

except ValueError:
    print("Please enter valid numbers!")

except ZeroDivisionError:
    print("can not divide by zero!")

