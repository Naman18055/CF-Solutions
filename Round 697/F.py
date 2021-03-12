def check():
	for i in range(n):
		for j in range(n):
			if change[i][j]:
				if (x[i]+y[j])%2==0:
					return False
			else:
				if (x[i]+y[j])%2:
					return False
	return True


for nt in range(int(input())):
	n = int(input())
	a, b = [], []
	for i in range(n):
		a.append(list(input()))
	input()
	for i in range(n):
		b.append(list(input()))
	# if nt==17:
	# 	print (a, b)
	# 	continue
	change = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			if a[i][j]!=b[i][j]:
				change[i][j] = 1

	x, y = [0], []
	for i in range(n):
		if change[0][i]:
			y.append(1)
		else:
			y.append(0)
	for i in range(1, n):
		if change[i][0]:
			if y[0]==1:
				x.append(0)
			else:
				x.append(1)
		else:
			if y[0]==1:
				x.append(1)
			else:
				x.append(0)
	# for i in change:
	# 	print (*i)
	# print (x, y)
	if check():
		print ("YES")
		continue

	x, y = [1], []
	for i in range(n):
		if change[0][i]:
			y.append(0)
		else:
			y.append(1)
	for i in range(1, n):
		if change[i][0]:
			if y[0]==1:
				x.append(0)
			else:
				x.append(1)
		else:
			if y[0]==1:
				x.append(1)
			else:
				x.append(0)
	# print (x, y)
	if check():
		print ("YES")
		continue
	print ("NO")