import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = 0
	prev = a[0]
	for i in range(1,n):
		if a[i]>a[i-1]:
			prev = a[i]
			continue
		ans += (a[i-1]-a[i])
	print (ans)


