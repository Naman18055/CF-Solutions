for nt in range(int(input())):
	input()
	n, k = map(int,input().split())
	a = list(map(int,input().split()))
	t = list(map(int,input().split()))
	b = [[a[i], t[i]] for i in range(k)]
	b.sort()
	a = [b[i][0] for i in range(k)]
	t = [b[i][1] for i in range(k)]

	ans = []
	minn = 10**18
	j = 0
	for i in range(n):
		minn += 1
		if j<len(a) and a[j]==i+1:
			minn = min(minn, t[j])
			ans.append(minn)
			j += 1
		else:
			ans.append(minn)

	minn = 10**18
	ind = n-1
	j = k-1
	# print (a)
	# print (t)
	for i in range(n-1, -1, -1):
		minn += 1
		if j>=0 and a[j]==i+1:
			minn = min(minn, t[j])
			ans[ind] = min(ans[ind], minn)
			j -= 1
		else:
			ans[ind] = min(ans[ind], minn)
		ind -= 1

	print (*ans)

