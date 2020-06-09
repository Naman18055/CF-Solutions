for nt in range(int(input())):
	x,y = map(int,input().split())
	if y==x-1:
		print ("NO")
		continue
	print ("YES")