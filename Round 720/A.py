for nt in range(int(input())):
	a, b = map(int,input().split())
	if b==1:
		print ("NO")
		continue
	if b==2:
		print ("YES")
		print (a, a*3, a*4)
		continue

	print ("YES")
	print (a*(b-1), a, a*b)