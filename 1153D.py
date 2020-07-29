n = int(input())
dp = [1]*n
o = list(map(int,input().split()))
p = list(map(int,input().split()))
for i in range(n-1):
	p[i] -= 1
for i in p:
	dp[i] = 0
count = sum(dp)
# print (p,dp)
for i in range(n-2,-1,-1):
	# print (dp)
	if not o[p[i]]:
		dp[p[i]] += dp[i+1]
	else:
		if not dp[p[i]]:
			dp[p[i]] = dp[i+1]
		else:
			dp[p[i]] = min(dp[i+1],dp[p[i]])

print (count-dp[0]+1)