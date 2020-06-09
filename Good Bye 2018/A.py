l=list(map(int,input().split()))
y,b,r=l[0],l[1],l[2]
if b<=y:
	y2=b
	y1=b-1
	if r<=y2:
		y3=r
		y2=r-1
		y1=r-2
	else:
		y3=b+1
else:
	y1=y
	y2=y+1
	if r<=y2:
		y3=r
		y2=r-1
		y1=r-2
	else:
		y3=y+2
print (y1+y2+y3)