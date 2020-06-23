n,m=map(int,input().split())
if n==1:
	print (1)
	exit()
if n==2:
	if m==1:
		print (2)
	elif m==2:
		print (1)
	exit()
x=(n+1)//2
if m<x:
	print (m+1)
elif m==x:
	if n%2==1:
		print (m-1)
	else:
		print (m+1)
else:
	print (m-1) 