for nt in range(int(input())):
	string = input()
	n = len(string)
	r,s,p = 0,0,0
	for i in string:
		if i=="R":
			r += 1
		elif i=="S":
			s += 1
		else:
			p += 1
	new = [[r,"R"],[s,"S"],[p,"P"]]
	new.sort()
	win = new[-1][1]
	if win=="R":
		ans = "P"*n
	elif win=="P":
		ans = "S"*n
	else:
		ans = "R"*n
	print (ans)
