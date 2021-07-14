for nt in range(int(input())):
	input()
	k, n, m = map(int,input().split())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	lines = k
	i = j = 0
	ans = []
	flag = True
	while i<n or j<m:
		if i==n:
			if b[j]==0:
				lines += 1
			else:
				if b[j]>lines:
					flag = False
					break
			ans.append(b[j])
			j += 1
		elif j==m:
			if a[i]==0:
				lines += 1
			else:
				if a[i]>lines:
					flag = False
					break
			ans.append(a[i])
			i += 1
		else:
			if a[i]==0:
				lines += 1
				ans.append(a[i])
				i += 1
			elif b[j]==0:
				lines += 1
				ans.append(b[j])
				j += 1
			else:
				if a[i]<b[j]:
					if a[i]>lines:
						flag = False
						break
					ans.append(a[i])
					i += 1
				else:
					if b[j]>lines:
						flag = False
						break
					ans.append(b[j])
					j += 1
	if flag:
		print (*ans)
	else:
		print (-1)


