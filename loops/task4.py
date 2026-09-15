# genrate the first N fibonacci number 

n = int(input("Enter how many Fibonacci numbers: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a)
    a, b = b, a + b
    i = i + 1