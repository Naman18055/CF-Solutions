n = int(input())
a = list(map(int,input().split()))
if n==1:
	print (a[0])
	exit()
dp = [[[0,0],[0,0]] for i in range(n+1)]
dp[1][0][1] = -a[0]
dp[1][1][0] = a[0]
dp[1][1][1] = -10**18
for i in range(2,n+1):
	dp[i][0][1] = -a[i-1] + dp[i-1][0][1]
	dp[i][1][0] = a[i-1] + dp[i-1][1][0]
	dp[i][1][1] = max(a[i-1]+dp[i-1][0][1],-a[i-1]+dp[i-1][1][0],a[i-1]+dp[i-1][1][1],-a[i-1]+dp[i-1][1][1])
print (dp[-1][1][1])
