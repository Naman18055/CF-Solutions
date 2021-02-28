for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	sa = set(a)
	b  = []
	for i in range(1, 2*n+1):
		if i not in sa:
			b.append(i)
	sb = set(b)

	arr = []
	for i in range(1, 2*n+1):
		if i in sb:
			arr.append(1)
		else:
			arr.append(-1)
	ans = [0]
	for i in arr:
		ans.append(ans[-1]+i)

	print (n+1-max(ans)+min(ans))