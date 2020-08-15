for nt in range(int(input())):
	n = int(input())
	a = list(map(int,list(input())))
	p = [a[0]]
	for i in range(1,n):
		p.append(p[-1]+a[i])
	d = {}
	ans = 0
	diff = 0
	for i in range(n):
		if -diff in d:
			d[-diff] += 1
		else:
			d[-diff] = 1

		diff += (a[i]-1)
		if -diff in d:
			ans += d[-diff]

		# print (d,diff)

	print (ans)


