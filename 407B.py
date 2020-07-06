mod = 10**9+7
n = int(input())
a = list(map(int,input().split()))
if n==1:
	print (2)
	exit()
dp = [0 for i in range(n)]
dp[1] = 2
for i in range(2,n):
	dp[i] = (2*dp[i-1]+2-dp[a[i-1]-1])%mod
ans = (2*dp[-1]+2-dp[a[-1]-1])%mod
# print (dp)
print (ans)

