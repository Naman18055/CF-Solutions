import math
for nt in range(int(input())):
	n,k=map(int,input().split())
	if k==n:
		print (k+1)
		continue
	if k<n:
		print (k)
		continue
	print (k+math.ceil(k/(n-1))-1)
