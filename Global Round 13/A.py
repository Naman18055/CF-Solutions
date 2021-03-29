import sys
input = sys.stdin.readline

from collections import Counter
n, q = map(int,input().split())
a = list(map(int,input().split()))
c = Counter(a)
if 1 not in c:
	c[1] = 0
for i in range(q):
	x, y = map(int,input().split())
	if x==1:
		y -= 1 
		if a[y]==0:
			c[0] -= 1
			c[1] += 1
		else:
			c[1] -= 1
			c[0] += 1
		a[y] = 1-a[y]
	else:
		if y<=c[1]:
			print (1)
		else:
			print (0)

