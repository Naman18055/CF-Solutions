n,m=map(int,input().split())
a=[]
b=[]
for i in range(n):
	a.append(list(map(int,input().split())))
for i in range(n):
	b.append(list(map(int,input().split())))
while True:
	if a[0][0]!=b[0][0]:
		print("NO")
		break
	elif a[n-1][n-1]!=b[n-1][n-1]:
		print("NO")
		break
	for i in range(n):
		for j in range(m):
			if a[i][j]!=b[i][j]:
				if a[i][j]==b[i][j+1 if j<m-1 else 0]:
					print("NO")
					break
				elif a[i][j]==b[i][j-1]:
					print ("NO")
					break
				elif a[i][j]==b[i+1 if i<n-1 else 0][j]:
					print ("NO")
					break
				elif a[i][j]==b[i-1][j]:
					print ("NO")
					break
	print ("YES")
	break