mod = 10**9+7
for nt in range(int(input())):
	n, k = map(int,input().split())
	dp = [[0 for i in range(k+1)] for j in range(n+1)]
	for i in range(2, k+1):
		for j in range(1, n+1):
			dp[j][i] = (1 + dp[n-j][i-1] + dp[j-1][i])%mod
	print ((1+dp[n][k])%mod)