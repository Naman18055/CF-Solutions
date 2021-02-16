for nt in range(int(input())):
	n, q = map(int,input().split())
	a = input()
	p, s = [[0,0]], [[0,0]]
	for i in range(n):
		if a[i]=="0":
			p.append([p[-1][0]+1, p[-1][1]])
		else:
			p.append([p[-1][0], p[-1][1]+1])
	for i in range(n-1, -1, -1):
		if a[i]=="0":
			s.append([s[-1][0]+1, s[-1][1]])
		else:
			s.append([s[-1][0], s[-1][1]+1])
	s = s[::-1]

	for i in range(q):
		l, r = map(int,input().split())
		# print (p, s, p[l-1], s[r])
		if p[l-1][int(a[l-1])]>0 or (s[r][int(a[r-1])])>0:
			print ("YES")
		else:
			print ("NO")