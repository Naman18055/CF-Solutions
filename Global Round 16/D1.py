for nt in range(int(input())):
	n, m = map(int,input().split())
	ans = [0]*m
	a = list(map(int,input().split()))
	b = []
	for i in range(m):
		b.append([a[i], i])
	b.sort(key = lambda x : (x[0], -x[1]))
	a = []
	for i in range(m):
		a.append(b[i][1])

	done = {}
	ans = 0
	for i in a:
		for j in range(i):
			if j in done:
				ans += 1
		done[i] = 1
		# print (done)
	print (ans)
