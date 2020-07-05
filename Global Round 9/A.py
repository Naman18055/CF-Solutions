import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	for i in range(n):
		a[i] = abs(a[i])
	c1,c2 = 0,0
	for i in range(1,n):
		if a[i]-a[i-1]>0:
			c1 += 1
		elif a[i]-a[i-1]<0:
			c2 += 1
		else:
			c1 += 1
			c2 += 1
	if c1>=n//2 and c2>=n//2:
		print (*a)
		continue
	c = []
	for i in range(1,n):
		c.append(a[i]-a[i-1])
	# print (c)
	for i in range(0,n-1,2):
		if c[i]*c[i+1]>0:
			a[i+1] = -a[i+1]
	print (*a)
