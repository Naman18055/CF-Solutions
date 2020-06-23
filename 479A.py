a=int(input())
b=int(input())
c=int(input())
l=[a,b,c]
if l.count(1)==3:
	print (3)
elif l.count(1)==2:
	if b==1:
		if a==1:
			print (2*c)
		else:
			print (2*a)
	else:
		print (b+2)
elif l.count(1)==1:
	if a==1:
		print ((a+b)*c)
	elif c==1:
		print (a*(b+c))
	else:
		print (max(a*(b+c),(a+b)*c))
else:
	print (a*b*c)