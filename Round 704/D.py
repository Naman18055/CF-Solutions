a, b, k = map(int,input().split())
x = "1"*b+"0"*a
if a==0 or b==1:
	if not k:
		print ("Yes")
		print (x)
		print (x)
	else:
		print ("No")
elif k>a+b-2:
	print ("No")
else:
	print ("Yes")
	print (x)
	if a>=k:
		print ("1"*(b-1)+"0"*k+"1"+"0"*(a-k))
	else:
		print ("1"*(b-1-k+a)+"0"+"1"*(k-a)+"0"*(a-1)+"1")


