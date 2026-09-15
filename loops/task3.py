# find factorial of the number 

n = int(input("Enter a number: "))

factorial = 1
i = 1

while i <= n:
    factorial = factorial * i
    i = i + 1

print("Factorial =", factorial)