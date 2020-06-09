def gcd(x,y):
	while(y):
		x,y=y,x%y 
	return x 

n,m=map(int,input().split())
x1=list(map(int,input().split()))
x=[]
p=list(map(int,input().split()))
temp=x1[0]
for i in range(1,n):
	x.append(x1[i]-temp)
if len(x)>1:
	hcf=gcd(x[0],x[1])
	for i in range(2,n-1):
		hcf=gcd(hcf,x[i])
	flag=0
	for i in range(m):
		if hcf%p[i]==0:
			print ('YES')
			print (temp,end=" ")
			print (i+1)
			flag=1
			break
	if flag==0:
		print ('NO')
else:
	for i in range(m):
		if x[0]%p[i]==0:
			print ("YES")
			print (temp,end=' ')
			print (i+1)
			exit(0)
	print ("NO")
