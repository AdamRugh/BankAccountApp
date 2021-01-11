class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return "%s's account Balance: $%.2f" % (self.name, self.balance)

#Show balance of account
  def show_balance(self):
    return "Balance: $%.2f" % (self.balance)

#Deposit into account
  def deposit(self, amount):
    if amount <= 0:
      print("Some error message here")
      return
    else:
      print("Depositing: " + str(amount))
      self.balance += amount
      self.show_balance()

#Withdraw from account
  def withdraw(self, amount):
    if amount >= self.balance:
      print("Will overdraw account")
      return
    else:
      print("Withdrawing: " + str(amount))
      self.balance -= amount
      self.show_balance()

#Test: name of account is Adam
my_account = BankAccount("Adam")
print(my_account)
#Showing account balance
my_account.show_balance()
#Depositing $2000
my_account.deposit(2000)
#Withdrawing $1000
my_account.withdraw(1000)
#printing new balance
print(my_account)
