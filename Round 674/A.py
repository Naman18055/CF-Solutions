for nt in range(int(input())):
	a,b = map(int,input().split())
	if a<=2:
		print (1)
		continue
	print ((a-3)//b+2)