import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n,x = map(int,input().split())
	a = list(map(int,input().split()))
	s = 0
	minn = 10**18
	v = []
	e = []
	for i in range(n):
		c = 0
		k = a[i]
		while not k%x:
			k = k//x
			c += 1
		if c<minn:
			minn = c
			v = i

	for i in range(n):
		if i<v:
			s += (minn+2)*a[i]
		else:
			s += (minn+1)*a[i]

	print (s)