import sys
from collections import Counter
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = sorted(a)

	d = {}
	ans = "YES"
	for i in range(n):
		if a[i] in d:
			d[a[i]][i%2] += 1
		else:
			d[a[i]] = [0, 0]
			d[a[i]][i%2] += 1
	for i in range(n):
		d[b[i]][i%2] -= 1
	for i in d:
		if d[i][0]!=0 or d[i][1]!=0:
			ans = "NO"
	print (ans)



