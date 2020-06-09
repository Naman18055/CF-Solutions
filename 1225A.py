a,b = map(int,input().split())
if a==9 and b==1:
	print (9,10)
	exit()
if b<a or b-a>=2:
	print (-1)
else:
	if b==a:
		print (str(a)+"1",str(b)+"2")
	else:
		print (str(a)+"9",str(b)+"0")