n=int(input())
a=list(map(int,input().split()))
dp=[[0,0] for i in range(n+1)]
dp[1][0]=1
dp[1][1]=1
for i in range(2,n+1):
	if a[i-1]>a[i-2]:
		dp[i][0]=dp[i-1][0]+1
		dp[i][1]=dp[i-1][1]+1
	else:
		dp[i][0]=1
		dp[i][1]=1
	if i-3>=0 and a[i-1]>a[i-3]:
		dp[i][1]=max(dp[i][1],dp[i-2][0]+1)

# print (dp)
ans=0
for i in range(n+1):
	ans=max(ans,dp[i][0],dp[i][1])
print (ans)