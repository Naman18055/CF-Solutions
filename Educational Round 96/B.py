for nt in range(int(input())):
	n,k = map(int,input().split())
	a = list(map(int,input().split()))
	a.sort()
	if k==0:
		print (a[-1]-a[0])
	else:
		print (sum(a[n-k-1:]))