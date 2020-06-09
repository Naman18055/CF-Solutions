import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n,k=map(int,input().split())
	s=input()
	s1="RGB"
	dp=[[0,0,0] for i in range(n)]
	ans=10**18
	for i in range(3):
		for j in range(k):
			if s[j]!=s1[(i+j)%3]:
				dp[0][i]+=1
		ans=min(ans,dp[0][i])
		for j in range(1,n-k+1):
			if s[j-1]!=s1[(i+j-1)%3]:
				dp[j][i]+=(dp[j-1][i]-1)
			else:
				dp[j][i]+=dp[j-1][i]
			if s[j+k-1]!=s1[(i+j+k-1)%3]:
				dp[j][i]+=1
			ans=min(ans,dp[j][i])
	# print (dp)
	print (ans)


