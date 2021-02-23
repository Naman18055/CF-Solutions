for nt in range(int(input())):
	x, y = map(int,input().split())
	if nt==20100000:
		print (str(x)+str(y))
		exit()
	if x>y:
		print (y-1+(x-y), y)
	else:
		if x==1:
			print (0, y)
		else:
			print (x-1, y)
