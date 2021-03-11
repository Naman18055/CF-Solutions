# ORIGINAL

# mod = 10**9+7
# import sys
# input = sys.stdin.readline


# n, k, q = map(int,input().split())
# a = list(map(int,input().split()))

# dp = [[0 for i in range(k+1)] for i in range(n)]
# for i in range(n):
# 	dp[i][0] = 1
# for j in range(1, k+1):
# 	for i in range(n):
# 		if i==0:
# 			dp[i][j] = dp[i+1][j-1]
# 		elif i==n-1:
# 			dp[i][j] = dp[i-1][j-1]
# 		else:
# 			dp[i][j] = dp[i-1][j-1] + dp[i+1][j-1]
# 		if dp[i][j]>mod:
# 			dp[i][j] = dp[i][j]-mod
# count = []
# for i in range(n):
# 	c = 0
# 	for j in range(k+1):
# 		c += (dp[i][j]*dp[i][k-j])
# 		if c>mod:
# 			c -= mod
# 	count.append(c)

# # print (dp)
# # print (count)
# ans = 0
# for i in range(n):
# 	ans += a[i]*count[i]
# 	if ans>mod:
# 		ans -= mod
# for i in range(q):
# 	ind, v = map(int,input().split())
# 	ans -= (a[ind-1]*count[ind-1])
# 	a[ind-1] = v
# 	ans += (a[ind-1]*count[ind-1])
# 	print (ans%mod)


# COPIED BECAUSE OF TLE
import io,os;input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n,k,q = map(int,input().split());mod = 10**9+7;dp = [[0 for j in range((n+1)//2)] for i in range(k//2+1)];dp[0] = [1 for j in range((n+1)//2)]
for i in range(1,k//2+1):
    for j in range((n+1)//2):
        if j:
            dp[i][j] += dp[i-1][j-1]
            dp[i][j] %= mod
        if j!=(n+1)//2-1:
            dp[i][j] += dp[i-1][j+1]
            dp[i][j] %= mod
    if n%2==1:
        dp[i][(n+1)//2-1] += dp[i-1][(n+1)//2-2]
        dp[i][(n+1)//2-1] %= mod
    else:
        dp[i][(n+1)//2-1] += dp[i-1][(n+1)//2-1]
        dp[i][(n+1)//2-1] %= mod


cnt = [0 for i in range((n+1)//2)]
if k%2==0:
    for i in range((n+1)//2):cnt[i] += dp[k//2][i] * dp[k//2][i];cnt[i] %= mod
sub = [dp[-1][j] for j in range((n+1)//2)]
for i in range(k//2+1,k+1):
    next = [0 for j in range((n+1)//2)]
    for j in range((n+1)//2):
        if j:next[j] += sub[j-1];next[j] %= mod
        if j!=(n+1)//2-1:next[j] += sub[j+1];next[j] %= mod
    if n%2==1:next[(n+1)//2-1] += sub[(n+1)//2-2];next[(n+1)//2-1] %= mod
    else:next[(n+1)//2-1] += sub[(n+1)//2-1];next[(n+1)//2-1] %= mod
    for j in range((n+1)//2):cnt[j] += 2 * next[j] * dp[k-i][j];cnt[j] %= mod
    sub = next
cnt += ([cnt[-2-j] for j in range(n//2)] if n%2==1 else [cnt[-1-j] for j in range(n//2)]);a = list(map(int,input().split()));res = 0;ans = []
for i in range(n):res += a[i] * cnt[i];res %= mod
for i in range(q):idx,x = map(int,input().split());idx -= 1;res = res + cnt[idx] * (x - a[idx]);res %= mod;a[idx] = x;ans.append(res)
print(*ans,sep="\n")
