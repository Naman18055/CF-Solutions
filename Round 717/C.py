n = int(input())
a = list(map(int,input().split()))
s = sum(a)
if s%2:
	print (0)
	exit()

dp = [[0 for i in range(s+1)] for j in range(n)]
for i in range(n):
	dp[i][0] = 1
dp[0][a[0]] = 1

for i in range(1, n):
	for j in range(1, s+1):
		if j>a[i]:
			dp[i][j] = max(dp[i][j], dp[i-1][j-a[i]])
		dp[i][j] = max(dp[i][j], dp[i-1][j])

# for i in dp:
# 	print (*i)

if dp[-1][s//2]==0:
	print (0)
	exit()

m = 10**18
for i in range(n):
	b = bin(a[i])[2:][::-1]
	ind = b.index("1")
	if ind<m:
		m = ind
		ans = i
print (1)
print (ans+1)