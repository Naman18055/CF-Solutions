for nt in range(int(input())):
	n,m = map(int,input().split())
	mat = []
	for i in range(n):
		mat.append(list(map(int,input().split())))
	ans = 0
	for i in range(n):
		for j in range(m):
			a = sorted([mat[i][j],mat[n-i-1][j],mat[i][m-j-1],mat[n-i-1][m-j-1]])
			ans += abs(a[1]-mat[i][j])
			ans += abs(a[1]-mat[n-i-1][j])
			ans += abs(a[1]-mat[i][m-j-1])
			ans += abs(a[1]-mat[n-i-1][m-j-1])
	print (ans//4)
