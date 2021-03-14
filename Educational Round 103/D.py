import bisect
for nt in range(int(input())):
	n = int(input())
	s = input()
	r = []
	l = []
	for i in range(len(s)-1):
		if s[i]==s[i+1]:
			r.append(i)
	for i in range(len(s)-1, 0, -1):
		if s[i]==s[i-1]:
			l.append(i)
	l = l[::-1]

	if s[0]=="R":
		if not r:
			ans = [n+1]
		else:
			ans = [r[bisect.bisect_left(r, 0)]+2]
	else:
		ans = [1]

	# print (r)
	# print (l)
	for i in range(1, n+1):
		c = 1
		if i<n and s[i]=="R":
			if not r:
				c += (n-i)
			else:
				t = bisect.bisect_left(r, i)
				if t==len(r):
					c += (n-i)
				else:
					# print (bisect.bisect_left(r, i), len(r), n)
					c += (r[bisect.bisect_left(r, i)] - i + 1)
		if s[i-1]=="L":
			if not l:
				c += i
			else:
				t = bisect.bisect(l, i-1)
				# print (i, t, "L")
				if t!=0:
					c += (i - l[t-1])
				else:
					c += i
		ans.append(c)

	print (*ans)



