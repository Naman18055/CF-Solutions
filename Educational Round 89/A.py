for nt in range(int(input())):
	a,b = map(int,input().split())
	a,b = min(a,b),max(a,b)
	if a==0:
		print (0)
		continue
	b = min(b,2*a)
	print ((a+b)//3)