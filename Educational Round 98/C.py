for nt in range(int(input())):
	s = input()
	a, b = [], []
	ans = 0
	for i in s:
		if i=="(":
			a.append(i)
		elif i==")":
			if not a:
				continue
			else:
				ans += 1
				a.pop()
		elif i=="[":
			b.append(i)
		else:
			if not b:
				continue
			else:
				ans += 1
				b.pop()
	print (ans)