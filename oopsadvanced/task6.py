# create a bank system with SavingAccount and currentaccount

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print("Balance:", self.balance)


class SavingAccount(BankAccount):

    def add_interest(self):
        interest = self.balance * 5 / 100
        self.balance = self.balance + interest
        print("Interest added:", interest)


class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")


saving = SavingAccount(10000)
current = CurrentAccount(10000)

saving.show_balance()
saving.add_interest()
saving.show_balance()

current.show_balance()
current.withdraw(2000)
current.show_balance()