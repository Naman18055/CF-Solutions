n=int(input())
l=list(map(int,input().split()))
if n==1:
	print (1,1)
	exit()
if len(set(l))==1:
	if n==2:
		print (1,2)
	else:
		print (1,3)
	exit()
l.sort()
d={}
count=0
for i in range(n-1):
	if str(l[i]-1) not in d:
		d[str(l[i]-1)]=1
		count+=1
	elif l[i+1]==l[i]:
		if str(l[i]+1) not in d:
			d[str(l[i]+1)]=1
			count+=1
		else:
			if str(l[i]) not in d:
				d[str(l[i])]=1
			else:
				d[str(l[i]+1)]=1
	else:
		if str(l[i]) not in d:
			d[str(l[i])]=1
		elif str(l[i]+1) not in d:
			d[str(l[i]+1)]=1
if str(l[-1]-1) not in d:
	d[str(l[-1]-1)]=1
elif str(l[-1]) not in d:
	d[str(l[-1])]=1
elif str(l[-1]+1) not in d:
	d[str(l[-1]+1)]=1
ans2=len(d)

l=list(set(l))
l.sort()
n=len(l)
count=0
i=0
while i<n-1:
	if l[i]+1==l[i+1]:
		count+=1
		i+=2
	elif l[i]-1==l[i-1] and i>0:
		i+=1
	else:
		count+=1
		i+=1
if l[-2]+1!=l[-1]:
	count+=1
ans1=count
print (ans1,ans2)


