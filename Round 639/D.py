def ifpossible():
	for i in range(n):
		if "#" not in grid[i]:
			if len(col)==0:
				return False
		else:
			for j in range(m):
				if grid[i][j]=="#":
					first=j
					break
			for j in range(m-1,-1,-1):
				if grid[i][j]=="#":
					last=j
					break
			if "." in grid[i][first:last]:
				return False
	for i in range(m):
		for j in range(n):
			if grid[j][i]=="#":
				first=j
				break
		for j in range(n-1,-1,-1):
			if grid[j][i]=="#":
				last=j
				break
		for j in range(first,last):
			if grid[j][i]==".":
				return False
	return True

n,m=map(int,input().split())
grid=[]
flag=0
for i in range(n):
	grid.append(input())
	if not flag and "#" in grid[-1]:
		flag=1

if flag==0:
	print (0)
	exit()

col=[]
for i in range(m):
	flag=0
	for j in range(n):
		if grid[j][i]=="#":
			flag=1
			break
	if not flag:
		col.append(i)

if not ifpossible():
	print (-1)
	exit()