for nt in range(int(input())):
	n,x,a,b=map(int,input().split())
	print (min(abs(a-b)+x,n-1))