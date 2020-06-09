for nt in range(int(input())):
	a,b,c,d=map(int,input().split())
	x,y,x1,y1,x2,y2=map(int,input().split())
	up=d-c+y
	right=b-a+x
	if x1==x2:
		if a!=0 or b!=0:
			print ("NO")
			continue
	if y1==y2:
		if c!=0 or d!=0:
			print ("NO")
			continue
	if x<=x2 and x>=x1 and y<=y2 and y>=y1:
		if up<=y2 and up>=y1 and right<=x2 and right>=x1:
			print ("YES")
		else:
			print ("NO")
	else:
		print ("NO")