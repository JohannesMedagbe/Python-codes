#!/usr/bin/env python
"""
File OOP_ex3.py
"""
class Account:
    """
    Represents bank account details
    """
    def __init__(self, name, account_number, balance):
    # instantiate object of class Account
        self.name=name
        self.account_number=account_number
        self.balance=balance
        self.balance_acceptable()
        
    def balance_acceptable(self):
        # assert that minimum balance is met
        if self.balance < 5000:
            print("Sorry, the minimum balance for an account with us is 5000 ksh.")
            return False
        else:
            return True
            
    def check_balance(self):
        # check the account balance
        print("Dear customer, your balance is", self.balance)
    

class OperationAccount(Account):
    """
    Allow transactions and operations like checking, withdrawal if possible, sending messages for appropriate assistance, checking balance etc.
    Fields:name, balance
    """
    def __init__(self, name, account_number, balance, transaction_type, amount):
        super().__init__(name, account_number, balance)
        # instantiate object of type OperationAccount representing an operation on respective account
        self.transaction_type=transaction_type
        self.amount=amount
        self.withdrawal_transaction()
        
    
    def deposit_transaction(self):
        # make a deposit of a given amount by giving all the instructions at once
        if self.transaction_type =="deposit":
            print("The new balance of ", self.name, " account number ", self.account_number, " is: ", self.balance + self.amount)
        
    def withdrawal_transaction(self):
        # make a withdrawal of a given amount if possible by given all the instructions at once. Provides assistance message in case of more than 3 overdraw attempts.
        if self.transaction_type =="withdrawal" and self.balance_acceptable():
            operations_number=int(input("Number of attempts:"))
            for i in range(operations_number):
                if self.amount>self.balance:
                    print("You have attempted to withdraw more than you have. Please try again with an appropriate request sum :)")
                else:
                    self.balance -= self.amount
                    print("The new balance of ", self.name, " account number ", self.account_number, " is: ", self.balance)
                    operations_number -= 1
                
            if operations_number >= 3 and self.amount > self.balance:
                print("You have tried 3 or more times to withdraw more than you have in account. Please, visit one of our customer care to get a current account allowing for overdraft facility :)")
            
    

cardi=OperationAccount("Cardi Bororo", 1707885218, 3500, "withdrawal", 30000)
mcqueen=OperationAccount("Mcqueen Opiyo", 349655044, 250000, "withdrawal", 40000)
vicky=OperationAccount("Vicky Marion Akothee", 568490433, 5000, "withdrawal", 68494)
gladys=OperationAccount("Gladys Wa maria", 403043030, 10000, "withdrawal", 5433)
