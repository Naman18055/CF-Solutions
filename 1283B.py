for nt in range(int(input())):
	n,k=map(int,input().split())
	c=n//k
	print (c*k+min(k//2,n-c*k))