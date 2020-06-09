n,m=map(int,input().split())
mod=998244353
if n==3:
	print (((m*(m-1))//2)%(mod))
	exit()
num=[]
calc=[1]
for i in range(2,m-2):
	calc.append((calc[-1]*i)%mod)
print (calc)
for i in range(1,m-1):
	a=i*2
	k=1
	if (n>4):
		a=a*calc[i]
	num.append(a)
print (num)
ans=0
k=1
for i in range(len(num)-1,-1,-1):
	count=num[i]*(m-k)
	k+=1
	#print (count)
	ans+=(count%mod)
print (ans%mod)