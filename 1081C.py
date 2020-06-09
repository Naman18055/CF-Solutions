def calc(n,k):
	return (fact[n]*(pow(fact[n-k]*fact[k],mod-2,mod)))%mod

mod = 998244353
n,m,k = map(int,input().split())
fact = [1]
for i in range(1,2001):
	fact.append((fact[-1]*i)%mod)
print ((calc(n-1,k)*m*pow(m-1,k,mod))%mod)