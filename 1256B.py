for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = []
	i = 0
	while i<n:
		m = min(a[i:])
		ind = a.index(m)
		if ind == i:
			i += 1
			continue
		for j in range(ind,i,-1):
			a[j],a[j-1] = a[j-1],a[j]
		i = ind

	print (*a)