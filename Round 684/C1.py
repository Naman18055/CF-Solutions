def correct(x, y):
	ans.append([x+1, y+1, x+1, y+2, x+2, y+2])
	ans.append([x+1, y+1, x+2, y+1, x+2, y+2])
	ans.append([x+1, y+1, x+1, y+2, x+2, y+1])

for nt in range(int(input())):
	n,m = map(int,input().split())
	a, ans = [], []
	for i in range(n):
		a.append(list(map(int,list(input()))))
	for i in range(n-1):
		for j in range(m-1):
			if a[i][j]==1:
				correct(i, j)

	for i in range(n-1):
		if a[i][-1]==1:
			ans.append([i+1, m, i+2, m, i+1, m-1])
			ans.append([i+1, m, i+2, m, i+2, m-1])
			ans.append([i+1, m, i+1, m-1, i+2, m-1])

	for i in range(m-1):
		if a[-1][i]==1:
			ans.append([n, i+1, n-1, i+1, n-1, i+2])
			ans.append([n, i+1, n-1, i+1, n, i+2])
			ans.append([n, i+1, n-1, i+2, n, i+2])

	if a[-1][-1]==1:
		ans.append([n, m, n-1, m, n-1, m-1])
		ans.append([n, m, n-1, m, n, m-1])
		ans.append([n, m, n-1, m-1, n, m-1])

	print (len(ans))
	for i in ans:
		print (*i)

