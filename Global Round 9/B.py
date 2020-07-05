def count(a,b):
	ans = 0
	if a+1<n and grid[a+1][b]:
		ans += 1
	if a-1>=0 and grid[a-1][b]:
		ans += 1
	if b+1<m and grid[a][b+1]:
		ans += 1
	if b-1>=0 and grid[a][b-1]:
		ans += 1
	return ans

def nb(a,b):
	ans = 0
	if a+1<n:
		ans += 1
	if a-1>=0:
		ans += 1
	if b+1<m:
		ans += 1
	if b-1>=0:
		ans += 1
	return ans

for nt in range(int(input())):
	n,m = map(int,input().split())
	grid = []
	for i in range(n):
		grid.append(list(map(int,input().split())))
	flag = 0
	for i in range(n):
		for j in range(m):

			if grid[i][j]>nb(i,j):
				flag = 1
				break

		if flag:
			break
	if flag:
		print ("NO")
	else:
		print ("YES")
		for i in range(n):
			for j in range(m):
				grid[i][j] = nb(i,j)
		for i in range(n):
			print (*grid[i])


