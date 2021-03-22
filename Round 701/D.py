n, m = map(int,input().split())
a = []
for i in range(n):
	a.append(list(map(int,input().split())))
b = [[720720 for i in range(m)] for j in range(n)]
for i in range(n):
	for j in range(m):
		if (i+j)%2:
			b[i][j] += pow(a[i][j], 4)
for i in b:
	print (*i)