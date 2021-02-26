import sys
mod = 10**9+7
input = sys.stdin.readline

def calc(n, r):
	return (fact[n]*pow(fact[r]*fact[n-r], mod-2, mod))%mod

fact = [1, 1]
for i in range(2, 2*10**5+10):
	fact.append((fact[-1]*i)%mod)
for nt in range(int(input())):
	n, m, k = map(int,input().split())
	a = list(map(int,input().split()))
	a.sort()
	i, j = 0, 0
	ans = 0
	# print (a)
	while i<len(a):
		while j<n and a[j]-a[i]<=k:
			j += 1
		if (j-i-1)>=m-1:
			# print (i, j, m)
			ans += calc(j-i-1, m-1)
			ans = ans%mod
		i += 1

	print (ans)
