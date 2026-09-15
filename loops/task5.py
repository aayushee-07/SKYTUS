# check if a number is prime 

number = int(input("Enter a number: "))

i = 2
is_prime = True

if number <= 1:
    is_prime = False

while i < number:
    if number % i == 0:
        is_prime = False
        break
    i = i + 1

if is_prime:
    print("The number is prime")
else:
    print("The number is not prime")