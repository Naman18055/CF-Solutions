mod=998244353
n=int(input())
ans=[-1]*n
ans[-1]=10
for i in range(n-2,-1,-1):
	ans[i]=((11+9*(n-i-1))*((9*pow(10,n-i-2,mod))%mod))%mod
print (*ans)