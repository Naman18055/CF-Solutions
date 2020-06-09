n,k=(map(int,input().split()))
k=k-1
l1=[0 for i in range(n)] #Not visited
l2=[1 for i in range(n)] #Number of rocks
count=-1
if n-k>k:
	left=1
else:
	left=0
while 0 in l1:
	#print (l1,l2,k,count)
	if l1[k]==0:
		count+=1
		if 0 in l2:
			l2[l2.index(0)]=l2[k]
		else:
			l2[k-1]+=1
		count+=l2[k]
		l1[k]=1
		count+=1
		l2[k]=0
		if k>0 and left==1:
			k=k-1
		elif k==0:
			k=k+1
			left=0
		elif k==n-1:
			k=k-1
			left=1
		else:
			k=k+1
	else:
		count+=1
		if left==1:
			k=k-1
		else:
			k=k+1
print (count)

