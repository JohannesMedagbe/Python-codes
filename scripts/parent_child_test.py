#!/usr/bin/env python

class EducationInstitution:
    def __init__(self, country, name):
        self.country=country
        self.name=name
    
    def getName(self):
        return self.name
    

class University(EducationInstitution):
    
    def __str__(self):
        return "The education institution " + self.name + " is a University."
    
    
class Student:
    
    def __init__(self, surname, firstname):
        self.surname=surname
        self.firstname=firstname
    
    def getIdentity(self):
        return self.surname + " " + self.firstname
    
class GraduateStudent(Student):
    
    def __init__(self, surname, firstname, graduate_course):
        super().__init__(surname, firstname)
        self.graduate_course=graduate_course
    
    def getFullInfo(self):
        return self.surname + " " + self.firstname + " is doing " + self.graduate_course
    
    
    
pwani=University("Kenya", "Pwani University")
print(pwani.__str__())

johannes=GraduateStudent("Medagbe", "Johannes", "MSc Bioinformatics")
print(johannes.getFullInfo())
