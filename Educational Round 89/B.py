for nt in range(int(input())):
	n,x,m = map(int,input().split())
	a = []
	for i in range(m):
		l,r = map(int,input().split())
		a.append((l,r))
	s,e = x,x
	for i in range(m):
		l,r = a[i][0],a[i][1]
		if s>=l and s<=r:
			s = min(s,l)
		if e>=l and e<=r:
			e = max(e,r)
	print (e-s+1)