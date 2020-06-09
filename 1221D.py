import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n=int(input())
	h=[]
	c=[]
	for i in range(n):
		a,b=map(int,input().split())
		h.append(a)
		c.append(b)
	dp=[[0,0,0,0] for i in range(n+1)]
	dp[1][1]=0
	dp[1][2]=c[0]
	dp[1][3]=c[0]*2
	for i in range(2,n+1):
		if h[i-1]==h[i-2]:
			dp[i][1]=min(dp[i-1][2],dp[i-1][3])
			dp[i][2]=min(dp[i-1][1],dp[i-1][3])+c[i-1]
			dp[i][3]=min(dp[i-1][1],dp[i-1][2])+2*c[i-1]
		elif h[i-1]+1==h[i-2]:
			dp[i][1]=min(dp[i-1][2],dp[i-1][1],dp[i-1][3])
			dp[i][2]=min(dp[i-1][2],dp[i-1][3])+c[i-1]
			dp[i][3]=min(dp[i-1][2],dp[i-1][1])+2*c[i-1]
		elif h[i-1]-1==h[i-2]:
			dp[i][1]=min(dp[i-1][1],dp[i-1][3])
			dp[i][2]=min(dp[i-1][1],dp[i-1][2])+c[i-1]
			dp[i][3]=min(dp[i-1][1],dp[i-1][2],dp[i-1][3])+2*c[i-1]
		else:
			x=min(dp[i-1][1],dp[i-1][2],dp[i-1][3])
			dp[i][1]=x
			dp[i][2]=x+c[i-1]
			dp[i][3]=x+2*c[i-1]
	# print (dp)
	print (min(dp[-1][1],dp[-1][2],dp[-1][3]))


