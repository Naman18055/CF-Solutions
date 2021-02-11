for nt in range(int(input())):
	n,m = map(int,input().split())
	a = []
	for i in range(n):
		a.append(list(map(int,input().split())))
	c = 0
	for i in range(n):
		for j in range(m):
			if a[i][j]<0:
				c += 1
	if c%2:
		s = 0
		minn = abs(a[0][0])
		for i in a:
			for j in i:
				s += abs(j)
				minn = min(minn, abs(j))
		print (s-2*minn)
	else:
		s = 0
		for i in a:
			for j in i:
				s += abs(j)
		print (s)
