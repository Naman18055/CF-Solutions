mod = 998244353
n = int(input())
s = [0]*(n+1)
for i in range(1, n+1):
	for j in range(i, n+1, i):
		s[j] += 1
ans = 0
temp = 0
for i in range(n+1):
	ans = temp + s[i]
	temp += ans
	ans = ans%mod
	temp = temp%mod
print (ans)
