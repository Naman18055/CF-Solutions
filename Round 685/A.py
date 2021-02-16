for nt in range(int(input())):
	n = int(input())
	if n==1:
		print (0)
	elif n==2:
		print (1)
	elif n==3:
		print (2)
	else:
		if n%2:
			print (3)
		else:
			print (2)