# fun to find GCD (Greatest Common Divisor) of two number

def gcd(a,b):
    while b:
        a,b = b , a % b

    return a 

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

print("GCD of two numbers= ",gcd(num1,num2))