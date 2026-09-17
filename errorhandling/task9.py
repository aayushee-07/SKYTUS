# write a program to log errors to a file instead of printing them 

try:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))

    result= num1 / num2
    print("You entered: ",result)

except ValueError as e:
    with open("error.log", "a") as file:
        file.write("ValueEroor: " + str(e) +"\n")

except ZeroDivisionError as e:
    with open ("error.log", "a") as file:
        file.write("ZeroDivisionError: " + str(e) + "\n")

finally:
    print("done!")
