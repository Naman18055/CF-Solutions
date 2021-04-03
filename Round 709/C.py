for nt in range(int(input())):
	n, m = map(int,input().split())
	a = []
	for i in range(m):
		a.append(list(map(int,input().split()))[1:])
	c = {}
	ans = [0]*m
	for i in range(m):
		ans[i] = a[i][0]
		if a[i][0] in c:
			c[a[i][0]] += 1
		else:
			c[a[i][0]] = 1
	maxx = 0
	for i in c:
		if c[i]>maxx:
			maxx = c[i]
			num = i
	if maxx<=(m-1)//2+1:
		print ("YES")
		print (*ans)
		continue
	for i in range(m):
		if maxx<=(m-1)//2+1:
			break
		if a[i][0]==num:
			for j in range(1, len(a[i])):
				if a[i][j]!=num:
					ans[i] = a[i][j]
					maxx -= 1
					break
	if maxx<=(m-1)//2+1:
		print("YES")
		print (*ans)
		continue
	print ("NO")
