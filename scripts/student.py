#!/usr/bin/python

"""
File:student.py
Resources to manage a student's name and test scores
"""
class Student():
	"""Represents student"""
	def __init__(self, name, number):
		"""Constructor creates a student with given name and number of scores and sets all the scores to 0."""
		self.name=name
		self.scores=[]
		for count in range(number):
			self.scores.append(0)
	def getName(self):
		"""Returns the student's name."""
		return self.name
	def setScores(self, i, score):
		"""Resets the ith score, counting from 1."""
		self.scores[i-1]=score
	def getScore(self, i):
		"""Returns the ith score, counting from 1."""
		return self.scores[i-1]
	def getAverage(self):
		"""Returns the average score."""
		return sum(self.scores) / len(self.scores)
	def getHighScore(self):
		"""Returns the highest score."""
		return max(self.scores)
	def __str__(self):
		"""Returns the string representation of the student."""
		return "Name:" + self.name + "\nScores:" + " ".join(map(str, self.scores))
p=Student("Parcelli", 4)
p.setScores(1, 80)
p.setScores(2, 70)
p.setScores(3, 90)
p.setScores(4, 55)
print(p.getName())
print(p.getHighScore())

i=Student("Isaya", 4)
i.setScores(1, 100)
i.setScores(2, 50)
i.setScores(3, 95)
i.setScores(4, 105)
print(i.getAverage())
print(i.getScore(3))
print(i.__str__())

lst=[i, p]
for x in lst:
	print(x.getName())
	
help(Student)
