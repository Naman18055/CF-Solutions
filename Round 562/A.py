n,a,x,y,b=map(int,input().split())
while a!=x and y!=b:
	if a==y:
		print ("YES")
		exit(0)
	else:
		if a<n:
			a+=1
		else:
			a=1
		if y>1:
			y-=1
		else:
			y=n
if a==y:
	print ("YES")
else:
	print ("NO")