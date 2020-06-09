for nt in range(int(input())):
	x,y=map(int,input().split())
	if x==3 or x==2:
		if y<=3:
			print ("YES")
		else:
			print ("NO")
	elif x==1:
		if y<=x:
			print ("YES")
		else:
			print ("NO")
	else:
		print ("YES")