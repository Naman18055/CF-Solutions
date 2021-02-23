for nt in range(int(input())):
	n, p, k = map(int,input().split())
	s = input()
	x, y = map(int,input().split())
	ans = 10**18
	for i in range(p, min(n+1, p+k)):
		v = (i-p)*y
		for j in range(i, n+1, k):
			if s[j-1]=="0":
				v += x
		ans = min(ans, v)
		# print (v)
		for j in range(i+k, n+1, k):
			v += (k*y)
			if s[j-k-1]=="0":
				v -= x
			ans = min(ans, v)
	print (ans)
