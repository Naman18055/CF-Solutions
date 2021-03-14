import math
for nt in range(int(input())):
	n, k = map(int,input().split())
	print ((((n+k-1)//k)*k+n-1)//n)