for nt in range(int(input())):
	n = int(input())
	s = input()
	if "L" not in s or "R" not in s:
		if n<=2:
			print (0)
		else:
			print ((n+2)//3)
		continue

	g = []
	curr = s[0]
	count = 1
	for i in range(1,n):
		if s[i]==curr:
			count += 1
		else:
			curr = s[i]
			g.append(count)
			count = 1
	g.append(count)
	
	# print (*g)
	if s[0]!=s[-1]:
		ans = 0
		for i in g:
			ans += i//3
		print (ans)
	else:
		g[0] += (g[-1])
		g[-1] = 0
		ans = 0
		for i in g:
			ans += i//3
		print (ans)
