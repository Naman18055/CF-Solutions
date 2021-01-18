for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	m = 10**9
	c = 0
	for i in range(n):
		if a[i]==1:
			break
		c += 1
	c2 = 0
	for i in range(n-1, -1, -1):
		if a[i]==1:
			break
		c2 += 1
	print (a.count(0)-c-c2)