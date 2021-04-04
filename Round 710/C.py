for nt in range(int(input())):
	a = input()
	b = input()
	maxx = 0
	for i in range(len(a)):
		for j in range(i, len(a)):
			if a[i:j+1] in b:
				maxx = max(maxx, j-i+1)
	print (len(a)+len(b)-maxx-maxx)