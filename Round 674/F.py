mod = 10**9+7
n = int(input())
s = input()
k = s.count("?")
dp = [[0 for i in range(6)] for j in range(k)]
dp[-1][0] = dp[-1][1] = dp[-1][2] = 1
for i in range(k-2,-1,-1):
	dp[i][0] = 2*dp[i+1][0] + 1 # a
	dp[i][1] = 2*dp[i+1][1] + 1 # b
	dp[i][2] = 2*dp[i+1][2] + 1 # c
	dp[i][3] = (dp[i+1][3] + (k-i-1)*pow(2,(k-i-2),mod))%mod # bc
	dp[i][4] = (dp[i+1][4] + (k-i-1)*pow(2,(k-i-2),mod))%mod # ab
	dp[i][5] = (dp[i+1][5] + dp[i+1][3])%mod # abc
for i in dp:
	print (*i)
