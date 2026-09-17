# use finally for resourse cleanup

try:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))

    result= num1 / num2
    print("You entered: ",result)

except ValueError:
    print("Please enter valid numbers!")

except ZeroDivisionError:
    print("can not divide by zero!")

finally:
    print("Done!")