# fun to check amstrong number

def armstrong(num):
    total = 0
    original = num

    while num > 0:
        digit = num % 10
        total = total + digit ** 3
        num = num // 10

    return total == original


number = int(input("Enter a number: "))

if armstrong(number):
    print("Armstrong number")
else:
    print("Not an Armstrong number")