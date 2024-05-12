#!/usr/bin/env python
"""
File OOP_ex1.py with set of classes for representing Employees, Managers and Clerks objects and manipulating them
"""
class Employee :
    """Base class to create an object of class Employee"""
    def __init__(self, name, pf_number, nhif_number, nssf_number, salary):
        self.name=name
        self.pf_number=pf_number
        self.nhif_number=nhif_number
        self.nssf_number=nssf_number
        self.salary=salary


class Manager(Employee):
    """Child class Manager inheriting constructor from base class Employee"""
    def __init__(self, name, pf_number, nhif_number, nssf_number, salary):
        super().__init__(name, pf_number, nhif_number, nssf_number, salary)
    
    def calc_salary_month(self):
        # calculate the monthly salary of the manager
        return self.salary + 0.02*25000000/12
        
    def __str__(self):
        # gives a string representation of manager name and his take home month salary
        return "The monthly salary of this manager " + self.name + " is: " + str(round(self.calc_salary_month(),2))
        
        
class Clerk(Employee):
    """Child class Clerk inheriting constructor from base class Employee"""
    def __init__(self, name, pf_number, nhif_number, nssf_number, salary):
        super().__init__(name, pf_number, nhif_number, nssf_number, salary)
    
    def calc_salary_month(self):
        # calculate the monthly salary of the clerk
        return self.salary + 0.1*self.salary
        
    def __str__(self):
        # gives a string representation of clerk name and his take home month salary
        return "The monthly salary of this clerk " + self.name + " is: " + str(round(self.calc_salary_month(),2))
        
kevin=Manager("Kevin", 1, 1, 1, 250000)
josephine=Clerk("Josephine", 2, 2, 2, 60000)
print(kevin.__str__())
print(josephine.__str__())
help(Clerk)
