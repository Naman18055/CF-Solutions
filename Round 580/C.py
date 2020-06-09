n=int(input())
if n%2==0:
	print ("NO")
	exit(0)
else:
	print ("YES")
	l=[-1]*(2*n)
	l[0]=1
	l[-1]=2*n
	k=1
	for i in range(1,n-1,2):
		k=k+3
		l[i]=k
		k=k+1
		l[i+1]=k
	k=-1
	for i in range(n,2*n-1,2):
		k=k+3
		l[i]=k
		k=k+1
		l[i+1]=k
	print (*l)
