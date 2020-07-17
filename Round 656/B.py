import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	d = {}
	ans = []
	for i in range(2*n):
		if a[i] not in d:
			d[a[i]] = 1
			ans.append(a[i])
	print (*ans)