for nt in range(int(input())):
	n,x=map(int,input().split())
	l=list(map(int,input().split()))
	if x in l:
		print (1)
		continue
	a=max(l)
	if a>x:
		print (2)
	else:
		if x%a==0:
			print (x//a)
		else:
			print (x//a+1)
		