for nt in range(int(input())):
	n, k = map(int,input().split())
	if n%2:
		print (1, n//2, n//2)
	else:
		if n//2%2:
			print (2, n//2-1, n//2-1)
		else:
			print (n//2, n//4, n//4)