mod = 10**9+7

def calc(n, r):
	return (fact[n]*pow((fact[r]*fact[n-r])%mod, mod-2, mod))%mod

fact = [1, 1]
for i in range(2, 10000):
	fact.append((fact[-1]*i)%mod)
for nt in range(int(input())):
	n, k = map(int,input().split())
	a = sorted(list(map(int,input().split())))[::-1]
	num = a[k-1]
	for i in range(n):
		if a[i]==num:
			count = i
			break
	print (calc(a.count(num), k-count))
