for nt in range(int(input())):
	n,m = map(int,input().split())
	mat = []
	for i in range(n):
		mat.append(list(input()))

	ans = 0
	for i in range(n-1,-1,-1):
		for j in range(m-1,-1,-1):
			if i==n-1 and m==-1:
				continue
			if i==n-1 and mat[i][j]=="D":
				ans += 1
			if j==m-1 and mat[i][j]=="R":
				ans += 1
	print (ans)

