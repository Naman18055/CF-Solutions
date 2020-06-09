mod = 998244353
n,k=map(int,input().split())
a = list(map(int,input().split()))
l = {}
for i in range(n):
	l[a[i]] = i
g = []
for i in range(n-k+1,n+1):
	g.append(l[i])
g.sort()
ans = 1
for i in range(1,len(g)):
	ans *= (g[i]-g[i-1])
	ans %= mod
print (sum(sorted(a)[n-k:]),ans)