n=int(input())
a=list(map(int,input().split()))
z, o = [], []

for i in range(n):
	if a[i]:
		o.append(i)
	else:
		z.append(i)
b1, b2 = len(z), len(o)
dp = [[10**18 for i in range(b2+1)] for j in range(b1+1)]
dp[0][0] = 0
for i in range(b1):
	for j in range(b2):
		dp[i+1][j] = min(dp[i+1][j], dp[i][j])
		dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+abs(z[i]-o[j]))
minn = 10**18
for i in range(b1+1):
	minn = min(minn, dp[i][-1])
print(minn)
