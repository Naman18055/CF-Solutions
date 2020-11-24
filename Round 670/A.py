import sys
from collections import Counter
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	c = Counter(a)
	flag = 0
	ans = 0
	for i in range(max(a)+2):
		if c[i]==1:
			if not flag:
				ans = i
				flag = 1
		elif c[i]==0:
			if not flag:
				ans = 2*i
			else:
				ans += i
			break
	print (ans)