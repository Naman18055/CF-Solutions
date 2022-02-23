for nt in range(int(input())): 
	s = list(input())
	x = sorted(s)
	b = ""
	done = 0
	for i in s:
		if i==x[0] and not done:
			done = 1
		else:
			b += i
	print (x[0], b)
