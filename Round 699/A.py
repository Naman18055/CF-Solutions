from collections import Counter
for nt in range(int(input())):
	x, y = map(int,input().split())
	s = input()
	c = Counter(s)
	u, d, r, l = 0, 0, 0, 0
	if x>0:
		r += x
	else:
		l += abs(x)
	if y>0:
		u += y
	else:
		d += abs(y)
	ans = "YES"
	for i in c:
		if i=="U":
			if c[i]<u:
				ans = "NO"
		elif i=="D":
			if c[i]<d:
				ans = "NO"
		elif i=="R":
			if c[i]<r:
				ans = "NO"
		else:
			if c[i]<l:
				ans = "NO"
	if "U" not in c and u>0:
		ans = "NO"
	if "D" not in c and d>0:
		ans = "NO"
	if "R" not in c and r>0:
		ans = "NO"
	if "L" not in c and l>0:
		ans = "NO"
	print (ans)