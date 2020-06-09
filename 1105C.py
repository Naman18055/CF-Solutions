mod = 10**9+7
n,l,r=map(int,input().split())
if l==r:
	if n%3==0:
		print (1)
	else:
		print (0)
	exit()
dp = [[0,0,0] for i in range(n)]
dp[0][0] = r//3-l//3
dp[0][1] = (r-1)//3-(l-1)//3
dp[0][2] = (r-2)//3-(l-2)//3
dp[0][l%3] += 1
for i in range(1,n):
	dp[i][0] = (dp[i-1][1]*dp[0][2]+dp[i-1][0]*dp[0][0]+dp[i-1][2]*dp[0][1])%mod
	dp[i][1] = (dp[i-1][1]*dp[0][0]+dp[i-1][0]*dp[0][1]+dp[i-1][2]*dp[0][2])%mod
	dp[i][2] = (dp[i-1][0]*dp[0][2]+dp[i-1][2]*dp[0][0]+dp[i-1][1]*dp[0][1])%mod
# print (dp)
print ((dp[-1][0])%mod)