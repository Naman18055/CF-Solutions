for nt in range(int(input())):
	a,b=map(int,input().split())
	if str(b).count("9")==len(str(b)):
		print (a*len(str(b)))
	else:
		print (a*(len(str(b))-1))
