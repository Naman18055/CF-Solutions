n,c=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dp=[[0,c] for i in range(n)]
for i in range(1,n):
	dp[i][0]=min(dp[i-1][0],dp[i-1][1])+a[i-1]
	dp[i][1]=min(dp[i-1][0]+c+b[i-1],dp[i-1][1]+b[i-1])
ans=[]
for i in range(n):
	ans.append(min(dp[i][0],dp[i][1]))
print (*ans)
