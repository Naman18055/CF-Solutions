for nt in range(int(input())):
	n = int(input())
	a = []
	X, Y = [], []
	for i in range(n):
		x, y = map(int,input().split())
		a.append([x, y])
		X.append(x)
		Y.append(y)
	X.sort()
	Y.sort()
	if n%2:
		print (1)
		continue

	x = X[n//2]-X[n//2-1]+1
	y = Y[n//2]-Y[n//2-1]+1
	print (x*y)