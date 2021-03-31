import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a, b = [], []
	for i in range(2*n):
		x, y = map(int,input().split())
		if x==0:
			a.append(abs(y))
		else:
			b.append(abs(x))
	a.sort()
	b.sort()
	ans = 0
	for i in range(n):
		ans += ((a[i]**2+b[i]**2)**0.5)
	print (ans)