for nt in range(int(input())):
	a,b,c = map(int,input().split())
	a1,a2 = -1,-1
	if a<c:
		a1 = 1
	if c==a:
		a2 = b
	else:
		if a*b>c:
			a2 = b
	print (a1,a2)