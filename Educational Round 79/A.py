for nt in range(int(input())):
	r,g,b=map(int,input().split())
	a=[r,g,b]
	a.sort()
	if (a[2]>(1+a[0]+a[1])):
		print ("No")
	else:
		print ("Yes")