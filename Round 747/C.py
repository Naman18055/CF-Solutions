for nt in range(int(input())):
	n, c = input().split()
	n = int(n)
	s = input()
	if s.count(c)==n:
		print (0)
		continue
	if s[-1]==c:
		print (1)
		print (n)
		continue
	if c not in s:
		print (2)
		print (n-1, n)
		continue
	a = []
	for i in range(n):
		if s[i]!=c:
			a.append(i+1)
	ans = a[0]-1
	for i in range(len(a)-1, -1, -1):
		if a[i]!=n-(len(a)-i-1):
			ans = n-len(a)+i+1
			break
	if ans*2<=n:
		print (2)
		print (n-1, n)
	else:
		print (1)
		print (ans)

