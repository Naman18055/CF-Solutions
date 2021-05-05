n, m, k = map(int,input().split())
left = []
for i in range(n):
	left.append(list(map(int,input().split())))
down = []
for i in range(n-1):
	down.append(list(map(int,input().split())))
if k%2:
	for i in range(n):
		for j in range(m):
			print (-1, end=" ")
		print ()
	exit()

dp = [[[10**7]*(k//2+1) for i in range(m)] for j in range(n)]
for i in range(n):
	for j in range(m):
		dp[i][j][0] = 0
		if j>0:
			dp[i][j][1] = min(dp[i][j][1], left[i][j-1])
		if i>0:
			dp[i][j][1] = min(dp[i][j][1], down[i-1][j])
		if i<n-1:
			dp[i][j][1] = min(dp[i][j][1], down[i][j])
		if j<m-1:
			dp[i][j][1] = min(dp[i][j][1], left[i][j])

for dist in range(2, k//2+1):
	for i in range(n):
		for j in range(m):
			if j>0:
				dp[i][j][dist] = min(dp[i][j][dist], dp[i][j-1][dist-1]+left[i][j-1])
			if i>0:
				dp[i][j][dist] = min(dp[i][j][dist], dp[i-1][j][dist-1]+down[i-1][j])
			if i<n-1:
				dp[i][j][dist] = min(dp[i][j][dist], dp[i+1][j][dist-1]+down[i][j])
			if j<m-1:
				dp[i][j][dist] = min(dp[i][j][dist], dp[i][j+1][dist-1]+left[i][j])

# for i in dp:
# 	print (*i)

for i in range(n):
	for j in range(m):
		print (2*dp[i][j][k//2], end=" ")
	print ()
