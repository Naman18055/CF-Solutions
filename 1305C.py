n,mod = map(int,input().split())
a = list(map(int,input().split()))
new = [-1]*n
for i in range(n):
	new[i] = a[i]%mod
if len(set(new))!=n:
	print (0)
else:
	a.sort(reverse=True)
	m = 1
	for i in range(n):
		for j in range(i+1,n):
			m = (m*(a[i]-a[j]))%mod
	print (m%mod)


