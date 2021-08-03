import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = [0] + list(map(int,input().split())) + [0]
	ans = 0
	for i in range(1, n+1):
		ans = max(ans, a[i]*a[i-1])
	print (ans)