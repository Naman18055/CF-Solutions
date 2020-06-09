# import sys
# input = sys.stdin.readline
mod = 10**9+7
n = int(input())
a = list(map(int,raw_input().split()))
fact = [[1] for i in range(1000001)]
b = max(a)
for i in range(2,b+1):
	for j in range(i,b+1,i):
		fact[j].append(i)
dp = [0]*(n+1)
dp[0] = 1
# dp[1] = n
for i in range(n):
	for j in range(len(fact[a[i]])-1,-1,-1):
		if fact[a[i]][j]<=i+1:
			dp[fact[a[i]][j]] = (dp[fact[a[i]][j]]%mod + dp[fact[a[i]][j]-1]%mod)%mod
	# print (dp)
	# print (count)
# print (dp)
print (sum(dp[1:])%mod)