import re
for nt in range(int(input())):
	a,b = map(int,input().split())
	s = input()
	s = re.sub("^0+(?!$)", "", s)
	new = s[0]
	for i in range(1, len(s)):
		if s[i]=="1" and s[i-1]=="1":
			continue
		else:
			new += s[i]
	s = re.sub("^0+(?!$)", "", new[::-1])
	s = s[::-1]
	n = len(s)
	g = []
	c = 0
	for i in range(1,n):
		if s[i]=="0":
			c += 1
		else:
			if c:
				g.append(c)
			c = 0
	if "1" not in s:
		print (0)
		continue
	ans = a
	for i in g:
		if i*b<a:
			ans += i*b
		else:
			ans += a
	print (ans)