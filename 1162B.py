n,m=map(int,input().split())
mat1=[]
mat2=[]
for i in range(n):
	mat1.append(list(map(int,input().split())))
for i in range(n):
	mat2.append(list(map(int,input().split())))
for i in range(n):
	for j in range(m):
		if mat1[i][j]<mat2[i][j]:
			mat1[i][j],mat2[i][j]=mat2[i][j],mat1[i][j]
for i in range(n):
	for j in range(1,m):
		if mat1[i][j]<=mat1[i][j-1]:
			print ("Impossible")
			exit(0)
		if mat2[i][j]<=mat2[i][j-1]:
			print ("Impossible")
			exit(0)
for i in range(1,n):
	for j in range(m):
		if mat1[i][j]<=mat1[i-1][j]:
			print ("Impossible")
			exit(0)
		if mat2[i][j]<=mat2[i-1][j]:
			print ("Impossible")
			exit(0)
print ("Possible")
