n,m = map(int,input().split())
mat = []
for i in range(n):
	mat.append(list(map(int,input().split())))
flag = 0
for i in range(n-1,-1,-1):
	for j in range(m-1,-1,-1):
		if mat[i][j]==0:
			mat[i][j] = min(mat[i+1][j]-1,mat[i][j+1]-1)
			if mat[i][j]<=mat[i-1][j] or mat[i][j]<=mat[i][j-1]:
				flag = 1
				break
		else:
			if (i<n-1 and mat[i][j]>=mat[i+1][j]) or (j<m-1 and mat[i][j]>=mat[i][j+1]):
				flag = 1
				break
			if (i>0 and mat[i][j]<=mat[i-1][j]) or (j>0 and mat[i][j]<=mat[i][j-1]):
				flag = 1
				break
	if flag:
		break
if flag:
	print (-1)
	exit()
s = 0
for i in range(n):
	for j in range(m):
		s += mat[i][j]
print (s)