import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	s = 0
	ans = 0
	for i in range(n):
		if a[i]<0:
			ans += max(0,-(s+a[i]))
			s += a[i]
			s = max(s,0)
		else:
			s += a[i]
	print (ans)