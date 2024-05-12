
# This module comprises python functions developed for advanced programming MSc Bioinformatics Pwani University

# compute and return the bonus_payment of an employee based on overtime, absent hours

def bonus_payment(name, overtime, absent):
	rep={range(41, 1000):50, range(31, 41):40, range(21, 31):30, range(11, 21):20, range(0, 11):10}
	num_hours=int(overtime-((2/3)*absent))
	for i in rep.keys():
		if num_hours in i:
			print("The bonus payment for", name, "is $", rep[i])

# check if a series of three numbers contains any 0

def zero_check(n1, n2, n3):
	if n1==0 or n2==0 or n3==0:
		print(True)
	else:
		print(False)
	
	
# check if series of 3 numbers is in order

def ordered3(n1, n2, n3):
	if n1<=n2<=n3:
		print(True)
	else:
		print(False)
	

# find the numbers of words between 1 and n evenly divisible by m

def modCount(m, n):
	assert m>=0, "m should be positive"
	assert n>=0, "n should be positive too"
	assert m<=n, "m should be smaller or equal to n"
	x=0
	for i in range(1, n+1):
		if i%m==0:
			x+=1
	print(x)
	
# print summary of sandwich items from one parameter

def sum_sandwich(items):
	for i in items:
		print(i);print("+")
	print("nothing more")
	
sum_sandwich(["magarin", "sardines", "fried eggs"])


