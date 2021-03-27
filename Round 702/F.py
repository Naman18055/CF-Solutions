from collections import Counter
import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	c = Counter(a)
	a = []
	for i in c:
		a.append(c[i])
	a.sort()
	n = len(a)
	p = [a[0]]
	s = [a[-1]]
	for i in range(1, n):
		p.append(p[-1]+a[i])
	for i in range(n-2, -1, -1):
		s.append(s[-1]+a[i])
	s = s[::-1]
	ans = s[0]-(n*a[0])
	for i in range(1, n):
		ans = min(ans, p[i-1]+s[i]-a[i]*(n-i))
	print (ans)

