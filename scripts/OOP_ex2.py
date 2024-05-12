#!/usr/bin/env python
"""
File OOP_ex2.py for manipulating base class and superclass and test method overriding
"""

class Policy:
    """Represents object of base class Policy"""
    def __init__(self, name, year_birth, salary):
        self.name=name
        self.year_birth=year_birth
        self.salary=salary
    
    def policyName(self):
        # gives policy name
        return self.name
    
    def maturityDate(self):
        # gives expiration date of the policy
        return self.year_birth + 40
    
        
    def premiumCalculator(self):
        # return the subscription amount
        return self.salary*0.15
    
class BimaPolicy(Policy):
    def __init__(self, name, year_birth, salary):
        super().__init__(name, year_birth, salary)
    
    def maturityDate(self):
        # gives expiration date of the policy
        return self.year_birth + 20
    
    def premiumCalculator(self):
        # return the subscription amount
        return self.salary*0.35
    
    
nyumbayangu=Policy("nyumbaYangu", 2010, 60000)
maxreturns=BimaPolicy("MaxReturns", 2010, 60000)
print("The maturity date for nyumbaYangu policy is: ", nyumbayangu.maturityDate())
print("The maturity date for MaxReturns policy is: ", maxreturns.maturityDate())
print("The subscription planned for nyumbaYangu is: ", nyumbayangu.premiumCalculator())
print("The subscription planned for MaxReturns is: ", maxreturns.premiumCalculator())
