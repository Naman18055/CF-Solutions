import sys
input = sys.stdin.readline

r,g,b = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
z = list(map(int,input().split()))
x.sort(reverse=True)
y.sort(reverse=True)
z.sort(reverse=True)
dp = [[[0 for i in range(b+1)] for j in range(g+1)] for k in range(r+1)]
dp[0][1][1] = y[0]*z[0]
dp[1][0][1] = x[0]*z[0]
dp[1][1][0] = x[0]*y[0]

for i in range(1,r):
	for j in range(1,g):
		dp[i][j][0] = max(dp[i][j][0],dp[i-1][j-1][0]+x[i-1]*y[j-1])

for i in range(r+1):
	for j in range(g+1):
		for k in range(1,b+1):
			dp[i][j][k] = dp[i][j][k-1]
			if j!=0:
				dp[i][j][k] = max(dp[i][j-1][k-1]+(y[j-1]*z[k-1]),dp[i][j][k],dp[i][j-1][k])
			if i!=0:
				dp[i][j][k] = max(dp[i-1][j][k-1]+(x[i-1]*z[k-1]),dp[i][j][k],dp[i-1][j][k])
			if i!=0 and j!=0:
				dp[i][j][k] = max(dp[i][j][k],dp[i-1][j-1][k]+(x[i-1]*y[j-1]))

# for i in dp:
# 	print (*i)

print (dp[r][g][b])