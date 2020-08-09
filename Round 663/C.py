mod = 10**9+7

def func(i):
	if i==0:
		return 1
	return (fact[n-1]*(pow((fact[i]*fact[n-1-i]),mod-2,mod))%mod)%mod

def calc():
	return pow(2,n-1,mod)

n = int(input())
fact = [1,1]
for i in range(2,n+1):
	fact.append((fact[-1]*i)%mod)
ans = fact[n]
# for i in range(n):
# 	left = i
# 	right = n-i-1
# 	ans = (ans-func(i))%mod
print ((ans-calc())%mod)