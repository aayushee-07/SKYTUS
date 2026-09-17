# write a program to written invalid integer input 

try:
    number= int(input("Enter the integer: "))
    print("you entered:", number)

except ValueError:
    print("Invalid input! Please enter an integer")

