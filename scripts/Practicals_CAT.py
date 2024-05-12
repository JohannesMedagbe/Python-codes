

def modify(lst):
	nlst=[]
	for i in lst:
		if i > 100:
			lst.append("over")
		elif i < 0:
			nlst.append("invalid")
		else:
			nlst.append(i)
	print(nlst)
	return nlst
	
	
modify([-10, 0, 25, 150, 78, 100, 1000, -1250])
modify([9, 20, 100])
modify([-1, 10, 99, 15000, 45])
modify([99, 0, T, -5])
