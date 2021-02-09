mod = 998244353
n = int(input())
a = sorted(list(map(int,input().split())))
c = 0
for i in range(n):
	c += abs(a[i]-a[2*n-i-1])
f = [1, 1]
for i in range(2, 2*n+1):
	f.append((f[-1]*i)%mod)
# print (f, c)
print ((c*(f[2*n]*pow((f[n]*f[n])%mod, mod-2, mod))%mod)%mod)