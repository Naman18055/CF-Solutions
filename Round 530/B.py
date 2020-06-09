n=int(input())
ans=0
if n==1:
	print (2)
elif n==2:
	print (3)
elif n==3:
	print (4)
else:
	x=n**(0.5)
	if x-(int(x))>0:
		x=int(x)
		x=x+1
	else:
		x=int(x)
	y=2*x
	if (x**2)-(x-1)<=n:
		ans=y
	else:
		ans=y-1
	print (ans)