# Object Oriented Programming Challenge

'''
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
'''

class Account:
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')

    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")

    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: ${self.balance}'

acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)