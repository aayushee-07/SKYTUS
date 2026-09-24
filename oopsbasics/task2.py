# create a bankaccount class with deposite and withdraw method 

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Balance:", self.balance)
        else:
            print("Insufficient balance")


ba1 = BankAccount(50000)

print("Initial balance:", ba1.balance)

ba1.deposit(10000)
ba1.withdraw(5000)