for nt in range(int(input())):
	a, b, c, d = map(int,input().split())
	e, f = max(a, b), max(c, d)
	l = [a, b, c, d]
	l.sort()
	e, f = max(e, f), min(e, f)
	if l[-1]==e and l[-2]==f:
		print ("YES")
	else:
		print ("NO")