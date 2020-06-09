n=int(input())
a=list(map(int,input().split()))
if n==1:
	print (0)
	exit(0)
dp=[[[10**9,10**9] for i in range(n+1)] for j in range(n+1)]
dp[0][0][0]=0
dp[0][0][1]=0
even,odd=0,0
for i in range(1,n+1):
	for j in range(1,n+1):
		if a[i-1]==0 or a[i-1]%2:
			dp[i][j][0]=min(dp[i-1][j-1][0],dp[i-1][j-1][1]+1)
	for j in range(n+1):
		if a[i-1]==0 or (not a[i-1]%2):
			dp[i][j][1]=min(dp[i-1][j][0]+1,dp[i-1][j][1])
	# if i<=10:
	# 	for i in dp:
	# 		print (*i)
	# 	print ()
if a[-1]==0:
	print (min(dp[n][n-n//2][0],dp[n][n-n//2][1]))
elif a[-1]%2:
	print ((dp[n][n-n//2][0]))
else:
	print ((dp[n][n-n//2][1]))
