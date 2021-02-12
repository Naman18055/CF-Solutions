for nt in range(int(input())):
	n, c0, c1, h = map(int,input().split())
	s = input()
	if c0<c1:
		if c0+h<c1:
			print (s.count("1")*h + n*c0)
		else:
			print (s.count("1")*c1 + s.count('0')*c0)
	else:
		if c1+h < c0:
			print (s.count("0")*h + n*c1)
		else:
			print (s.count("1")*c1 + s.count('0')*c0)