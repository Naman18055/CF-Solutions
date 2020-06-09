n,b,a=map(int,input().split())
ib=b
ia=a
l=list(map(int,input().split()))
count=0
i=0
while (a!=0 or b!=0) and i<n:
	if a==ia:
		a-=1
	else:
		if a==0:
			if l[i]==1:
				a+=1
			b-=1
		elif b==0:
			a-=1
		else:
			if l[i]==0:
				a-=1
			elif l[i]==1:
				b-=1
				a+=1
	i+=1
print (i)