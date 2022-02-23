import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n, k = map(int,input().split())
	a = list(map(int,input().split()))
	k += 1
	for i in range(n):
		a[i] = pow(10, a[i])
	res = 0
	for i in range(n):
		count = k
		if (i+1<n):
			count = min(count, a[i+1]//a[i] - 1)
		res += a[i]*count
		k -= count
	print (res)