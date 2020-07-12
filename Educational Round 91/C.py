for nt in range(int(input())):
	n,x = map(int,input().split())
	a = list(map(int,input().split()))
	a.sort(reverse=True)
	i = 0
	ans = 0
	p = 1
	c = 0
	while i<n:
		c += 1
		p = c*a[i]
		if p>=x:
			ans += 1
			c = 0
		i += 1

	print (ans)