for nt in range(int(input())):
	n, k = map(int,input().split())
	a = list(map(int,input().split()))
	i = 0
	while k:
		while i<n and a[i]==0:
			i += 1
		if i>=n-1:
			break
		if k>a[i]:
			a[-1] += a[i]
			k -= a[i]
			a[i] = 0
		else:
			a[i] -= k
			a[-1] += k
			k = 0
	print (*a)