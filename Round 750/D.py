import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if n%2:
		b = [0]*n
		for i in range(n//2-1):
			b[i] = -a[n-i-1]
			b[n-i-1] = a[i]
		if a[n//2-1]+a[n//2+1]:
			b[n//2-1] = -a[n//2]
			b[n//2+1] = -a[n//2]
			b[n//2] = a[n//2-1]+a[n//2+1]
		else:
			b[n//2-1] = -a[n//2]
			b[n//2+1] = a[n//2]
			b[n//2] = a[n//2-1]-a[n//2+1]
		print (*b)
	else:
		b = [0]*n
		for i in range(n//2):
			b[i] = -a[n-i-1]
			b[n-i-1] = a[i]
		print (*b)