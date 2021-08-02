for nt in range(int(input())):
	n, k = map(int,input().split())
	b = {}
	for i in range(k):
		x, y = map(int,input().split())
		b[x] = y
		b[y] = x

	for i in range(1, 2*n+1):
		if i in b:
			continue
		o = []
		for j in range(1, 2*n+1):
			if i!=j and j not in b:
				o.append(j)
		b[i] = o[len(o)//2]
		b[o[len(o)//2]] = i

	# print (b)
	ans = 0
	for i in range(1, 2*n+1):
		for j in range(1, 2*n+1):
			if i!=j:
				if b[i]>i:
					if j<b[i] and j>i and b[j]>b[i]:
						ans += 1
				else:
					if j<i and j>b[i] and b[j]>i:
						ans += 1
	print (ans//2)



