mod=998244353
n=int(input())
fact=[1,1]
for i in range(2,n+1):
	fact.append((fact[-1]*i)%mod)
ans=0
sub=n
for i in range(n-2):
	ans+=(((fact[n]-sub)%mod))
	sub=(sub*(n-i-1))%mod
	ans=ans%mod
# print (ans)
# ans=(ans*n)%mod
# print (ans)
ans+=fact[n]
print ((ans)%mod)