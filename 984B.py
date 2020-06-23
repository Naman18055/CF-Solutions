def bomb(i,j):
	num = 0
	for di in range(-1, 2):
		for dj in range(-1, 2):
			if di != 0 or di != dj:
				x, y = i + di, j + dj
				if x >= 0 and x < n and y >= 0 and y < m and matrix[x][y] == '*':
					num += 1
	return num

n,m=map(int,input().split())
matrix=[]
for i in range(n):
	matrix.append(list(input()))
ans="YES"
for i in range(n):
	for j in range(m):
		if matrix[i][j]==".":
			count = bomb(i,j)
			if count!=0:
				ans="NO"
				break
		elif matrix[i][j]!="." and matrix[i][j]!="*":
			count = bomb(i,j)
			if count!=int(matrix[i][j]):
				ans="NO"
				break
	if ans=="NO":
		break
print (ans)