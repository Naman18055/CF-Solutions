for nt in range(int(input())):
	n = int(input())
	a = []
	for i in range(n):
		a.append(list(input()))
	b = []
	for i in range(n):
		for j in range(n):
			if a[i][j]=="*":
				b.append((i, j))
	if b[0][0]!=b[1][0] and b[1][1]!=b[0][1]:
		a[b[0][0]][b[1][1]] = "*"
		a[b[1][0]][b[0][1]] = "*"
	elif b[0][0]==b[1][0]:
		if b[0][0]!=0:
			a[b[0][0]-1][b[0][1]] = "*"
			a[b[0][0]-1][b[1][1]] = "*"
		else:
			a[b[0][0]+1][b[0][1]] = "*"
			a[b[0][0]+1][b[1][1]] = "*"
	else:
		if b[1][1]!=0:
			a[b[0][0]][b[1][1]-1] = "*"
			a[b[1][0]][b[1][1]-1] = "*"
		else:
			a[b[0][0]][b[1][1]+1] = "*"
			a[b[1][0]][b[1][1]+1] = "*"

	for i in range(n):
		print ("".join(a[i]))