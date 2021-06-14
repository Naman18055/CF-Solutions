for nt in range(int(input())):
	n, m = map(int,input().split())
	grid = []
	for i in range(n):
		grid.append(list(input()))

	ans = [[0 for i in range(m)] for j in range(n)]
	possible = True
	for i in range(n):
		for j in range(m):
			if (i+j)%2 and grid[i][j]=="W":
				possible = False
				break
			elif (i+j)%2==0 and grid[i][j]=="R":
				possible = False
				break

			if (i+j)%2:
				ans[i][j] = "R"
			else:
				ans[i][j] = "W"
	if possible:
		print ("YES")
		for i in range(n):
			print ("".join(ans[i]))
		continue

	ans = [[0 for i in range(m)] for j in range(n)]
	possible = True
	for i in range(n):
		for j in range(m):
			if (i+j)%2 and grid[i][j]=="R":
				possible = False
				break
			elif (i+j)%2==0 and grid[i][j]=="W":
				possible = False
				break

			if (i+j)%2:
				ans[i][j] = "W"
			else:
				ans[i][j] = "R"
	if possible:
		print ("YES")
		for i in range(n):
			print ("".join(ans[i]))
		continue

	print ("NO")

