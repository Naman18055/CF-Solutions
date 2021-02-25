for nt in range(int(input())):
	n = int(input())
	a = []
	for i in range(n):
		a.append(list(input()))
	c = [0, 0, 0]
	for i in range(n):
		for j in range(n):
			if a[i][j]=="X":
				c[(i+j)%3] += 1
	r = c.index(min(c))
	for i in range(n):
		for j in range(n):
			if a[i][j]=="X" and (i+j)%3==r:
				a[i][j]="O"
	for i in a:
		print ("".join(i))
