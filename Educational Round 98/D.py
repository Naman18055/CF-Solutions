mod = 998244353
fact = [1, 1]
for i in range(2, 3*10**5):
	fact.append((fact[-1]*i)%mod)

def calc(n, k):
	# print (n, k, fact[n+k-1], fact[n-1])
	return fact[n+k-1]*pow(fact[n-1]*fact[k], mod-2, mod)

n = int(input())
ans = 0
for i in range(n%2, n+1, 2):
	if not i:
		continue
	one = i
	zero = (n-i)//2
	ans += calc(one, zero)
	ans = ans%mod
print ((ans*pow(pow(2, n, mod), mod-2, mod))%mod)

