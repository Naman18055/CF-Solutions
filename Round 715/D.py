for nt in range(int(input())):
	n = int(input())*2
	a = input()
	b = input()
	c = input()
	i, j, k = 0, 0, 0
	ans = ""
	while i!=n and j!=n and k!=n:
		if a[i]==b[j]==c[k]:
			ans += a[i]
			i += 1
			j += 1
			k += 1
		elif a[i]==b[j]:
			ans += a[i]
			i += 1
			j += 1
		elif a[i]==c[k]:
			ans += a[i]
			i += 1
			k += 1
		else:
			ans += b[j]
			j += 1
			k += 1
	if i==n:
		if j>k:
			ans += b[j:]
		else:
			ans += c[k:]
	elif j==n:
		if i>k:
			ans += a[i:]
		else:
			ans += c[k:]
	else:
		if i>j:
			ans += a[i:]
		else:
			ans += b[j:]
	print (ans)