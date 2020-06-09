n,mod=map(int,input().split())
fact=[1,1]
for i in range(2,n+1):
	fact.append((fact[-1]*i)%mod)
ans=0
for i in range(1,n+1):
	ans+=((n-i+1)*(fact[i]*fact[n-i+1])%mod)%mod
	ans=ans%mod
print (ans)