for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	dp = [[10**18 for i in range(2*n)] for j in range(n+1)]
	for i in range(2*n):
		dp[0][i] = 0
	for i in range(n):
		for j in range(2*n-1):
			dp[i+1][j+1] = min(dp[i+1][j], dp[i][j]+abs(j+1-a[i]))
	print (dp[-1][-1])