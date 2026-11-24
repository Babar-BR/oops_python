# 1. What is encapsulation?
# Encapsulation is an OOP concept that combines data (variables) and methods (functions) into a single unit (class) and controls access to that data.

# In simple words:

# Encapsulation helps protect data from being accessed or modified directly.
# 2. Why do we need encapsulation?
# We need encapsulation for three main reasons:
# 1. Data protection: Prevents unintended direct modification of data.
# 2. Controlled access: Allows us to decide how data can be accessed or modified.
# 3. Data validation: We can validate values before updating data.


class Bank:
  def __init__(self,balance):
    self.__balance=balance
  def credit(self,amount):
    if(amount>0):
      self.__balance+=amount
    else:
      print('invalid amount ')
  def get(self):
    print(f'balance is now={self.__balance}')
ob=Bank(1000)
ob.credit(500)
ob.get()
    