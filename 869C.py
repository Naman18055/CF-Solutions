def ncr(n,r):
	return (fact[n]*pow((fact[n-r]*fact[r])%mod,mod-2,mod))%mod

def calc(a,b):
	count=1
	count+=(a*b)
	for i in range(2,min(a,b)+1):
		# print (ncr(a,i))
		count=(count+(ncr(a,i)*ncr(b,i)*fact[i]))%mod
	return count

mod=998244353
fact=[1,1]
for i in range(2,5001):
	fact.append((fact[-1]*i)%mod)
a,b,c=map(int,input().split())
x1=calc(a,b)
x2=calc(b,c)
x3=calc(a,c)
# print (x1,x2,x3)
print ((x1*x2*x3)%mod)