for nt in range(int(input())):
	n,s = input().split()
	n = int(n)

	a = [i for i in range(n,0,-1)]
	i = 0
	c = []
	while i<n:
		if i<n-1 and s[i]=="<":
			start = i
			while start<n-1 and s[start]=="<":
				start += 1
			c.append((i,start))
			i = start
		else:
			i += 1
	j,i = 0,0
	ans = []
	while i<n:
		if j<len(c) and c[j][0]==i:
			for k in range(c[j][1],c[j][0]-1,-1):
				ans.append(a[k])
			i = c[j][1]+1
			j += 1
		else:
			ans.append(a[i])
			i += 1
	print (*ans)

	a = [i for i in range(1,n+1)]
	i = 0
	c = []
	while i<n:
		if i<n-1 and s[i]==">":
			start = i
			while start<n-1 and s[start]==">":
				start += 1
			c.append((i,start))
			i = start
		else:
			i += 1
	j,i = 0,0
	ans = []
	while i<n:
		if j<len(c) and c[j][0]==i:
			for k in range(c[j][1],c[j][0]-1,-1):
				ans.append(a[k])
			i = c[j][1]+1
			j += 1
		else:
			ans.append(a[i])
			i += 1
	print (*ans)
