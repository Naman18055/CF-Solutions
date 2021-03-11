import math
for nt in range(int(input())):
	s = input()
	t = input()
	if len(s)<len(t):
		s, t = t, s
	x, y = len(s), len(t)
	s = s+s
	ans = 0
	i = 0
	while i<x:
		if s[i:i+y]!=t:
			ans = -1
			break
		else:
			i += len(t)
	if ans==-1:
		print (ans)
		continue
	if s[-len(t):]!=t:
		print (-1)
		continue
	print (t*(((x*y)//math.gcd(x, y))//y))
