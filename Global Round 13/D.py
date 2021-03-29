def solve(u, v):
	a = bin(u)[2:]
	b = bin(v)[2:]
	# print (a, b)
	if b.count("1")>a.count("1"):
		return False
	c = 0
	for i in range(-1, -len(a), -1):
		if a[i]=="1":
			c += 1
		if b[i]=="1" and c==0:
			return False
		if b[i]=="1":
			c -= 1
	return True



for nt in range(int(input())):
	u, v = map(int,input().split())

	if u>v:
		print ("NO")
		continue

	if u%2==0 and v%2:
		print ("NO")
		continue

	if u%2 and v%2:
		u -= 1
		v -= 1
	if solve(u, v):
		print ("YES")
	else:
		print("NO")