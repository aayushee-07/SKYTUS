# display multiplication table for given number 

n = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(n, "*", i, "=", n * i)
    i = i + 1