import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n,p,k=map(int,input().split())
	a=list(map(int,input().split()))
	a.sort()
	if p<a[0]:
		print (0)
		continue
	dp=[[0,0] for i in range(n+1)]
	dp[0][1]=p
	dp[1][0]=1
	dp[1][1]=p-a[0]
	for i in range(2,n+1):
		if dp[i-1][1]>=a[i-1]:
			dp[i][0]=max(dp[i][0],dp[i-1][0]+1)
			dp[i][1]=dp[i-1][1]-a[i-1]
		if i>=k and dp[i-k][1]>=a[i-1]:
			dp[i][0]=max(dp[i][0],dp[i-k][0]+k)
			dp[i][1]=dp[i-k][1]-a[i-1]
	ans=0
	for i in range(1,n+1):
		ans=max(ans,dp[i][0])
	print (ans)