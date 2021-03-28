import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	c = {}
	for i in range(n):
		c[a[i]] = i
	maxx = n
	ans = []
	m = n
	while len(ans)!=n:
		if c[maxx]>m:
			maxx -= 1
			continue

		for i in range(c[maxx], m):
			ans.append(a[i])
		m = min(m, c[maxx])
		maxx -= 1
	print (*ans)
