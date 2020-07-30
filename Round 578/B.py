for nt in range(int(input())):
	n,m,k = map(int,input().split())
	a = list(map(int,input().split()))
	ans = "YES"
	for i in range(1,n):
		if a[i]<=a[i-1]:
			m += min(a[i-1],(a[i-1]-a[i])+k)
		elif a[i-1]>=a[i]-k:
			m += min(a[i-1],a[i-1]-(a[i]-k))
		else:
			m -= (a[i]-k-a[i-1])
		if m<0:
			ans = "NO"
			break
	print (ans)