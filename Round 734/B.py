for nt in range(int(input())):
	n, k = map(int,input().split())
	a = list(map(int,input().split()))
	b = [[] for i in range(n)]
	count = 0
	for i in range(n):
		if len(b[a[i]-1])<k:
			b[a[i]-1].append(i)
			count += 1
	total = count - count%k
	ans = [0]*n
	curr = 1
	count = 0
	flag = False
	for i in b:
		for j in i:
			ans[j] = curr
			curr += 1
			if curr>k:
				curr = 1
			count += 1
			if count==total:
				flag = True
				break
		if flag:
			break
	print (*ans)
