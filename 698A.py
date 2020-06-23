import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
dp = [[0 for i in range(3)] for j in range(n)]
dp[0][0] = 0
if a[0]==1 or a[0]==3:
	dp[0][1] = 1
if a[0]==2 or a[0]==3:
	dp[0][2] = 1
for i in range(1,n):
	dp[i][0] = max(dp[i-1])
	if a[i]==1 or a[i]==3:
		dp[i][1] = max(dp[i-1][0],dp[i-1][2])+1
	if a[i]==2 or a[i]==3:
		dp[i][2] = max(dp[i-1][0],dp[i-1][1])+1

m = 0
for i in dp:
	# print (*i)
	m = max(m,max(i))
print (n-m)