for nt in range(int(input())):
	n = int(input())
	a = []
	for i in range(n):
		a.append(list(map(int,list(input()))))
	minr, minc = [10**18 for i in range(10)], [10**18 for i in range(10)]
	maxr, maxc = [-1 for i in range(10)], [-1 for i in range(10)]
	for i in range(n):
		for j in range(n):
			x = a[i][j]
			minr[x] = min(minr[x], j)
			maxr[x] = max(maxr[x], j)
			minc[x] = min(minc[x], i)
			maxc[x] = max(maxc[x], i)
	ans = [0]*10
	for i in range(n):
		for j in range(n):
			x = a[i][j]
			ans[x] = max(ans[x], max(maxr[x] - j, j - minr[x]) * max(i, n - i - 1))
			ans[x] = max(ans[x], max(maxc[x] - i, i - minc[x]) * max(j, n - j - 1))
	print(*ans)
