for nt in range(int(input())):
	d, k = map(int,input().split())
	x = (((d**2)/2)**0.5)/k
	# print (x)
	# print ((k*x)**2, (k*(x+1))**2)
	if (k*int(x))**2 + (k*int(x+1))**2 <= d**2:
		print ("Ashish")
	else:
		print ("Utkarsh")