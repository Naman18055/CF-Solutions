for nt in range(int(input())):
	n,r = map(int,input().split())
	r = min(r,n)
	if n==r:
		print (((r+1)*r)//2-n+1)
	else:
		print (((r+1)*r)//2)