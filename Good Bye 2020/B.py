import sys
input = sys.stdin.readline
from collections import Counter

for nt in range(int(input())):
	n = int(input())
	a = sorted(list(map(int,input().split())))
	c = Counter(a)
	a = sorted(set(a))
	for i in a[::-1]:
		if i+1 not in c or c[i+1]==0:
			c[i+1] = 1
			c[i] -= 1
		elif c[i+1]>1:
			if c[i]!=1:
				c[i+1] += 1
				c[i] -= 1
		# print (c)
	ans = 0
	for i in c:
		if c[i]>=1:
			ans += 1
	print (ans)
