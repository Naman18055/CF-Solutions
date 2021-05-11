for nt in range(int(input())):
	n = int(input())
	u = list(map(int,input().split()))
	s = list(map(int,input().split()))
	c = {}
	for i in range(n):
		if u[i] not in c:
			c[u[i]] = [s[i]]
		else:
			c[u[i]].append(s[i])
	for i in c:
		c[i].sort()
	ans = []
	ans.append(sum(s))

	arr = [c[i] for i in c]
	arr.sort(key = lambda x: len(x))
	for i in arr:
		i.sort(reverse=True)
	v = [len(arr[i]) for i in range(len(arr))]
	suff = []
	for i in arr:
		suff.append([i[-1]])
		for j in range(len(i)-2, -1, -1):
			suff[-1].append(i[j]+suff[-1][-1])
		suff[-1] = suff[-1][::-1]
	# print (v)
	# print (arr)
	# print (suff)

	j = 0
	for i in range(2, n+1):
		curr = 0
		while j<len(v) and v[j]<i:
			j += 1
		for k in range(j, len(arr)):
			if v[k]%i!=0:
				curr += (suff[k][0] - suff[k][-(v[k]%i)])
			else:
				curr += suff[k][0]
			# print (v[k], i, curr)
		ans.append(curr)
	print (*ans)

