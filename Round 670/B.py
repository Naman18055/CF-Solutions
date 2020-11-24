import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	dp = [[[1,1],[1,1],[1,1],[1,1],[1,1]] for i in range(n)]
	dp[0][0][0] = dp[0][0][1] = a[0]
	for i in range(1,n):
		dp[i][0][0] = max(dp[i-1][0][0], a[i])
		dp[i][0][1] = min(dp[i-1][0][1], a[i])

	for i in range(1,5):
		dp[i][i][0] = dp[i][i][1] = dp[i-1][i-1][0]*a[i]
		for j in range(i+1,n):
			dp[j][i][0] = max(dp[j-1][i][0],dp[j-1][i-1][0]*a[j],dp[j-1][i-1][1]*a[j])
			dp[j][i][1] = min(dp[j-1][i][1],dp[j-1][i-1][0]*a[j],dp[j-1][i-1][1]*a[j])
	# for i in dp:
		# print (*i)
	print (dp[-1][-1][0])