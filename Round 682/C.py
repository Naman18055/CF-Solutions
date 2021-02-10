for nt in range(int(input())):
	n,m = map(int,input().split())
	a = []
	for i in range(n):
		a.append(list(map(int,input().split())))
	b = []
	for i in range(n):
		b.append([])
		for j in range(m):
			if a[i][j]%2!=(i+j)%2:
				b[-1].append(a[i][j]+1)
			else:
				b[-1].append(a[i][j])
	for i in b:
		print (*i)