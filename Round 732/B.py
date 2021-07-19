import sys

def diff(a, b):
	for i in a:
		if i not in b:
			return i
		if a[i]!=b[i]:
			return i

for nt in range(int(input())):
	n, m = map(int,input().split())
	a = []
	c = [{} for i in range(m)]
	for i in range(n):
		a.append(input())
		for j in range(m):
			if a[-1][j] not in c[j]:
				c[j][a[-1][j]] = 1
			else:
				c[j][a[-1][j]] += 1
	b = []
	d = [{} for i in range(m)]
	for i in range(n-1):
		b.append(input())
		for j in range(m):
			if b[-1][j] not in d[j]:
				d[j][b[-1][j]] = 1
			else:
				d[j][b[-1][j]] += 1
	ans = ""
	for i in range(m):
		ans += diff(c[i], d[i])
	print (ans)
