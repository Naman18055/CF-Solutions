n=int(input())
matrix=[[i for i in range(n)] for j in range(n)]
num=0
for i in range(n):
	for j in range(n):
		matrix[i][j]=num
		num+=1
answer=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
	for j in range(n):
		answer[i][j]=matrix[j][(i+j)%n]
for i in range(n):
	for j in range(n):
		print (answer[i][j],end=" ")
	print ()