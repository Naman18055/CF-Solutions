n = int(input())
a = sorted(list(map(int,input().split())))
dp = [0 for i in range(n)]
for i in range(n-1, -1, -1):
	for j in range(i+1, n):
		dp[j] = a[j] - a[i] + min(dp[j], dp[j-1])
print(dp[-1])
 
 
 