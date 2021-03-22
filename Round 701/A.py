import math
for nt in range(int(input())):
	a, x = map(int,input().split())
	if x==1:
		b = x+1
	else:
		b = x
	ans = a + 3
	while b<x+40:
		k = a
		c = b-x
		while k!=0:
			k = k//b
			c += 1
		ans = min(ans, c)
		b += 1
	print (ans)