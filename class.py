
#creating a class and construtor for storing bank account details 
class BankAccount:
  def __init__(self, account_number, account_holder_name, account_balance):
    self.account_number = account_number
    self.account_holder_name = account_holder_name
    self.account_balance = account_balance


# Usage:
account = BankAccount("12345", "subham", 200)
print(f"Account Number: {account.account_number}")
print(f"Account Holder Name: {account.account_holder_name}")
print(f"Account Balance: ${account.account_balance:.2f}")


#methods to deposit and withdraw the money.

class BankAccount:
   def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

   def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

   def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds for withdrawal.")
        else:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")

   def get_balance(self):
        return self.balance

# Example usage:
account = BankAccount("subham", 1000)

print(f"Account holder: {account.account_holder}")
print(f"Initial balance: ${account.get_balance()}")

account.deposit(500)
account.withdraw(200)
account.withdraw(800)

account.display_info()






