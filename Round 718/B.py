for nt in range(int(input())):
	n, m = map(int,input().split())
	a = []
	for i in range(n):
		a.append(list(map(int,input().split())))
	curr = a[0]
	curr = sorted(curr)
	j = 0
	ans = []
	for i in curr:
		ans.append([i, i])
	while j<n-1:
		nxt = a[j+1]
		ans.sort(key = lambda x:x[0])
		nxt = sorted(nxt)[::-1]
		# print (ans, nxt)
		for i in range(m):
			ans[i][0] = min(ans[i][0], nxt[i])
			ans[i].append(nxt[i])
		j += 1
	f = []
	for i in range(1, n+1):
		f.append([])
		for j in range(m):
			f[-1].append(ans[j][i])
	for i in f:
		print (*i)