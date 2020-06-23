n=int(input())
a=int(input())
b=int(input())
c=int(input())
if n==1:
	print (0)
elif n==2:
	print (min(a,b))
else:
	if a<b:
		print (a+min(a,c)*(n-2))
	else:
		print (b+min(c,b)*(n-2))
