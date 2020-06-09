import math
for nt in range(int(input())):
	n,g,b=map(int,input().split())
	if g>=math.ceil(n/2):
		print (n)
		continue
	print (max((math.ceil((math.ceil(n/2))/g)-1)*b+math.ceil(n/2),n))