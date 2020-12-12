mod = 10**9+7
s = list(map(int,list(input())))
n = len(s)
summ = sum(s[0:n-1])
num = (n*(n+1))//2
ans = 0
for i in range(1,n+1):
	num -= (n-i+1)
	ans += ((i*(summ)+(num*s[n-i]))*pow(10,i-1,mod))%mod
	# print (i,summ,num,ans)
	ans = ans%mod
	summ -= s[n-i-1]
print (ans)