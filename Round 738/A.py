import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = a[0]
	for i in range(1, n):
		ans = ans&a[i]
	print (ans)