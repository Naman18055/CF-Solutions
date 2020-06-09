n=int(input())
t=input()
s=''
for i in range(1,n):
	x=i*(i+1)/2
	x=x-1
	x=int(x)
	if x<n:
		s=s+t[x]
	else:
		break
if n==1:
	print (t)
else:
	print (s)
