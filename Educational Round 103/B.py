import sys
input = sys.stdin.readline

import math
for nt in range(int(input())):
	n, k = map(int,input().split())
	a = list(map(int,input().split()))
	s = a[0]
	ans = 0
	for i in range(1, n):
		diff = max(0, math.ceil((100*a[i])/k-s))
		ans += diff
		s += diff
		s += a[i]
	print (int(ans))

