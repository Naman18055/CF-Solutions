for nt in range(int(input())):
	n, u, v = map(int,input().split())
	a = list(map(int,input().split()))
	ans = 10**18
	for i in range(1, n):
		if abs(a[i]-a[i-1])>=2:
			ans = 0
		if abs(a[i]-a[i-1])==1:
			ans = min(ans, min(u, v))
		if a[i]==a[i-1]:
			ans = min(ans, v + min(u, v))
	print(ans)