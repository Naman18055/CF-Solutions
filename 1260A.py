for nt in range(int(input())):
	c,s=map(int,input().split())
	a=s//c
	b=s%c
	print ((c-b)*(a**2)+(b)*((a+1)**2))