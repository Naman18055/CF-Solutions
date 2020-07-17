for nt in range(int(input())):
	a = list(map(int,input().split()))
	a.sort()
	if len(set(a))==3:
		print ("NO")
	elif len(set(a))==1:
		print ("YES")
		print (a[0],a[0],a[0])
	else:
		if a[0]==a[1]:
			print ("NO")
		else:
			print ("YES")
			print (a[0],a[0],a[1])