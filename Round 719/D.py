import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	d = {}
	for i in range(n):
		if a[i]-i in d:
			d[a[i]-i] += 1
		else:
			d[a[i]-i] = 1
	# print (d)

	ans = 0
	for i in d:
		if d[i]>1:
			ans += (d[i]*(d[i]-1))//2
	print (ans)