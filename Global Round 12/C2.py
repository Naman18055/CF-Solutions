for nt in range(int(input())):
	n = int(input())
	a = []
	for i in range(n):
		a.append(list(input()))
	c = [0, 0, 0, 0, 0, 0]
	for i in range(n):
		for j in range(n):
			if a[i][j]=="X":
				c[(i+j)%3] += 1
			if a[i][j]=="O":
				c[3+(i+j)%3] += 1
	maxx = 10**18
	for i in range(3):
		for j in range(3):
			if c[i]+c[j+3]<maxx and i!=j:
				v = [i, j]
				maxx = c[i]+c[j+3]
	r1 = v[0]
	r2 = v[1]

	for i in range(n):
		for j in range(n):
			if a[i][j]=="X" and (i+j)%3==r1:
				a[i][j]="O"
			if a[i][j]=="O" and (i+j)%3==r2:
				a[i][j]="X"
	for i in a:
		print ("".join(i))
