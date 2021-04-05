for nt in range(int(input())):
	n = int(input())
	a = input()
	b = input()
	if a==b:
		print ("YES")
		continue
	c0 = []
	if a[0]=="0":
		c0.append(1)
	else:
		c0.append(0)
	for i in range(1, n):
		if a[i]=="0":
			c0.append(c0[-1]+1)
		else:
			c0.append(c0[-1])

	ans = "YES"
	inv = 0
	for i in range(n-1, -1, -1):
		if a[i]!=b[i]:
			if not inv:
				if 2*c0[i]!=i+1:
					ans = "NO"
					break
				inv = 1
		else:
			if inv:
				if 2*c0[i]!=i+1:
					ans = "NO"
					break
				inv = 0
		# print (i, a[i], b[i], inv)
	# print (c0)
	print (ans)


