n,m = map(int,input().split())
a = input()
b = input()
dp = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
	if a[i]==b[0]:
		dp[i][0] = 2
	else:
		dp[i][0] = max(0, dp[i-1][0] - 1)

for i in range(m):
	if b[i]==a[0]:
		dp[0][i] = 2
	else:
		dp[0][i] = max(0, dp[0][i-1] - 1)
for i in range(1, n):
	for j in range(1, m):
		if a[i]==b[j]:
			dp[i][j] = max(dp[i][j], dp[i-1][j-1]+2)
		else:
			dp[i][j] = max(dp[i][j], dp[i-1][j]-1, dp[i][j-1] - 1)
ans = 0
# for i in dp:
# 	print (*i)
for i in dp:
	for j in i:
		ans = max(ans, j)
print (ans)