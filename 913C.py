n,l = map(int,input().split())
a = list(map(int,input().split()))
for i in range(1,n):
	a[i] = min(a[i],2*a[i-1])
ans = 10**18
count = 0
for i in range(n-1,-1,-1):
	count += (a[i]*(l//(2**i)))
	l = l%(2**i)
	if l==0:
		ans = min(ans,count)
	else:
		ans = min(ans,count+a[i])
print (ans)