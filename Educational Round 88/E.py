mod=998244353

def func(n,k):
	return (fact[n]*(pow((fact[k]*fact[n-k])%mod,mod-2,mod)))%mod

n,k=map(int,input().split())
if k==1:
	print (n)
	exit(0)
fact=[1]
for i in range(1,1000001):
	fact.append((fact[-1]*i)%mod)
if k>n:
	print (0)
elif k==n:
	print (1)
else:
	ans=func(n-1,k-1)
	temp=n//k
	for i in range(2,temp+1):
		count=n//i
		# print (count,i,k)
		ans+=(func(count-1,k-1))
		ans=ans%mod
	print (ans)
