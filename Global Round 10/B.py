import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n,k = map(int,input().split())
	a = list(map(int,input().split()))
	for j in range(2):
		if j%2:
			maxx = max(a)
			for i in range(n):
				a[i] = maxx-a[i]
			odd = a[::]
		else:
			maxx = max(a)
			for i in range(n):
				a[i] = maxx-a[i]
			even = a[::]
	if not k%2:
		print (*odd)
	else:
		print (*even)
