for nt in range(int(input())):
	m = int(input())
	a = []
	a.append(list(map(int,input().split())))
	a.append(list(map(int,input().split())))

	if m==1:
		print (0)
		continue

	prefix = [[0 for i in range(m)] for j in range(2)]
	suffix = [[0 for i in range(m)] for j in range(2)]
	prefix[0][0] = a[0][0]
	prefix[1][0] = a[1][0]
	for i in range(1, m):
		prefix[0][i] = prefix[0][i-1] + a[0][i]
		prefix[1][i] = prefix[1][i-1] + a[1][i]
	suffix[0][-1] = a[0][-1]
	suffix[1][-1] = a[1][-1]
	for i in range(m-2, -1, -1):
		suffix[0][i] = suffix[0][i+1] + a[0][i]
		suffix[1][i] = suffix[1][i+1] + a[1][i]

	ans = min(suffix[0][1], prefix[1][-2])
	for i in range(1, m-1):
		ans = min(ans, max(prefix[1][i-1], suffix[0][i+1]))
	print (ans)

