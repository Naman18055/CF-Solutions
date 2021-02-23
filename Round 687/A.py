for nt in range(int(input())):
	n,m,r,c = map(int,input().split())
	print (max(r+c-2, n+m-r-c, n-r+c-1, m-c+r-1))