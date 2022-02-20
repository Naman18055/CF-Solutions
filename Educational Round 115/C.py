from collections import Counter

import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	c = Counter(a)
	k = sum(a)/n
	res = 0
	for i in range(n):
		c[a[i]] -= 1
		res += c[2*k - a[i]]
	print (res)