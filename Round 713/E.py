for nt in range(int(input())):
	n, l, r, s = map(int,input().split())
	m = r-l+1
	if (m*(m+1))//2>s or (n*(n+1))//2-((n-m)*(n+1-m))//2<s:
		print (-1)
		continue

	ans = [0]*n
	num = [i for i in range(1, m+1)]
	diff = s - (m*(m+1))//2
	maxx = n
	ind = -1
	while diff!=0:
		# print (num, maxx, ind, diff)
		if maxx-num[ind]<=diff:
			diff -= (maxx-num[ind])
			num[ind] = maxx
			ind -= 1
			maxx -= 1
		else:
			num[ind] += diff
			break
	ind = 0
	for i in range(l, r+1):
		ans[i-1] = num[ind]
		ind += 1
	s = set(num)
	v = 1
	for i in range(n):
		if ans[i]==0:
			while v in s:
				v += 1
			ans[i] = v
			v += 1
	print (*ans)

