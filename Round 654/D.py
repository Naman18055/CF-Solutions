for nt in range(int(input())):
	n,k = map(int,input().split())
	# n = 7
	if k==n**2:
		print (0)
		ans = []
		for i in range(n):
			ans.append("1"*n)
		for i in ans:
			print (i)
		continue

	minn = k//n
	maxx = minn+1
	cmaxx = k%n
	cminn = n-cmaxx

	count = 1
	ans = [[]]
	for i in range(n):
		if i<minn:
			ans[-1].append("1")
		else:
			ans[-1].append("0")
	cminn -= 1
	if cmaxx==0:
		print (0)
	else:
		print (2)
	prev = ans[-1].index("0")
	while cminn or cmaxx:
		ans.append([0]*n)
		flag = 0
		if cminn>0:
			nxt = 0
			for i in range(prev,prev+n):
				if i-prev<minn:
					ans[-1][i%n] = "1"
				else:
					if not flag:
						nxt = i%n
						flag = 1
					ans[-1][i%n] = "0"
			cminn -= 1
			prev = nxt
			continue

		if cmaxx>0:
			nxt = 0
			for i in range(prev,prev+n):
				if i-prev<maxx:
					ans[-1][i%n] = "1"
				else:
					if not flag:
						nxt = i%n
						flag = 1
					ans[-1][i%n] = "0"
			cmaxx -= 1
			prev = nxt

	for i in ans:
		print ("".join(map(str,i)))


