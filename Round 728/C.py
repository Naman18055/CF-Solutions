import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	ans = 0
	v = 0
	for i in range(2, n):
		v += a[i-2]
		ans -= (a[i]*(i-1))
		ans += v
	print (ans)