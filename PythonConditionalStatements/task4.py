# ATM withdrawal check: sufficient balance or not 

balance = int(input("Enter your balance: "))
withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")