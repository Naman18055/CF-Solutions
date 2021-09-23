for nt in range(int(input())):
	s = input()
	n = len(s)
	c = 0
	cont = False
	for i in range(n):
		if s[i]=="1":
			cont = False
		else:
			if not cont:
				cont = True
				c += 1
	print (min(c, 2))
