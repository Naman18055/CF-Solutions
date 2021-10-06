for nt in range(int(input())):
	n, m, upper = map(int,input().split())
	g = []
	d = []
	for i in range(n):
		g.append(list(input()))
		d.append([0]*m)
	for i in range(n):
		for j in range(m):
			if g[i][j]=="*" and d[i][j]==0:
				maxx = -1
				for k in range(min(i, j, m-j-1)+1):
					if g[i-k][j-k]=="*" and g[i-k][j+k]=="*":
						maxx += 1
					else:
						break
				if maxx>=upper:
					d[i][j] = 1
					for k in range(maxx+1):
						d[i-k][j-k] = 1
						d[i-k][j+k] = 1

	ans = "YES"
	for i in range(n):
		for j in range(m):
			if g[i][j]=="*" and d[i][j]==0:
				ans = "NO"
				break
	print (ans)


