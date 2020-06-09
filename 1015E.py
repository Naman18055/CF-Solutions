def possible(i,j):
	count = 0
	x = 10**18
	for k in range(j+1,m):
		if grid[i][k]=="*":
			count+=1
		else:
			break
	x = min(x, count)
	count = 0
	for k in range(j-1,-1,-1):
		if grid[i][k]=="*":
			count+=1
		else:
			break
	x = min(x, count)
	count = 0
	for k in range(i+1,n):
		if grid[k][j]=="*":
			count+=1
		else:
			break
	x = min(x, count)
	count = 0
	for k in range(i-1,-1,-1):
		if grid[k][j]=="*":
			count+=1
		else:
			break
	x = min(x, count)
	if x == 0:
		return -1
	for k in range(i-x,i+x+1):
		done[(k,j)] = 1
	for k in range(j-x,j+x+1):
		done[(i,k)] = 1
	return x

n, m = map(int,input().split())
grid = []
l = {}
for i in range(n):
	grid.append(input())
	for j in range(m):
		if grid[-1][j]=="*":
			l[(i,j)] = 1
done = {}
c = {}
for i in range(n):
	for j in range(m):
		if grid[i][j]=="*":
			x = possible(i,j)
			if x!=-1:
				c[(i,j)] = x
	if len(l) == len(done):
		break
if len(l)!=len(done):
	print (-1)
	exit()
print (len(c))
for i in c:
	print (i[0]+1,i[1]+1,c[i])
