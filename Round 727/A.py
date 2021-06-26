for nt in range(int(input())):
	n, x, t = map(int,input().split())
	c = min(n-1, t//x)
	print ((c)*(n-c-1) + (c*(c+1))//2)