import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n, m = map(int,input().split())
	a = list(map(int,input().split()))
	a.sort()
	b = list(map(int,input().split()))
	p = [b[0]]
	for i in range(1, m):
		p.append(p[-1]+b[i])
	ans = 10**18
	s = 0
	for i in range(n-m):
		s += b[a[i]-1]
	for i in range(max(0, n-m), n):
		ans = min(ans, s+p[n-i-1])
		s += b[a[i]-1]
	print (ans)