for nt in range(int(input())):
	s = input()
	n = len(s)
	if n==1:
		print (s[0])
		continue
	g = [[s[0],1]]
	prev = s[0]
	for i in range(1,n):
		if s[i]==prev:
			g[-1][1] += 1
		else:
			prev = s[i]
			g.append([prev,1])
	ans = []
	for i in g:
		if i[1]%2:
			ans.append(i[0])
	ans = list(set(ans))
	ans.sort()
	for i in ans:
		print (i,end="")
	print ()
