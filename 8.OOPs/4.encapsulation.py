# Demonstrates encapsulation using private/protected attributes

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # protected attribute
        self.__balance = balance              # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

# Usage
acc = BankAccount("12345", 1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.get_balance())

# Accessing protected vs private attributes
print("Account Number:", acc._account_number)    # works (convention: use carefully)
# print(acc.__balance)  # ❌ AttributeError (private variable)