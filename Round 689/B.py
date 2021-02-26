def calc(i, j):
	if i==0 or j==0 or j==m-1:
		return 0
	return min(c[i][j-1], c[i-1][j], c[i][j+1])


for nt in range(int(input())):
	n, m = map(int,input().split())
	a = []
	for i in range(n):
		a.append(list(input()))
	c = [[0 for i in range(m)] for j in range(n)]
	p = -1
	ans = 0
	curr = 1
	while curr!=min(n, m)+1:
		for i in range(curr-1, n):
			for j in range(curr-1, m-curr+1):
				# print (i, j)
				if a[i][j]=="*":
					x = calc(i, j)
					c[i][j] = x + 1
		curr += 1
	for i in range(n):
		for j in range(m):
			ans += c[i][j]
	print (ans)
