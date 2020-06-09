n=int(input())
l=list(map(int,input().split()))
new=[]
for i in range(n):
	if l[i]>=3:
		new.append(l[i])
odd=[0]*n
loc=[]
for i in range(len(new)):
	if new[i]%2==1 and new[i]>=3:
		odd[i]=1
		loc.append(i)
if len(loc)==0:
	c=l.count(1)
	print (sum(l)//2)
else:
	c=loc[-1]
	count=0
	count+=(sum(new[0:c]))//2
	count+=(sum(new[c:])-1)//2
	a=l.count(2)
	b=l.count(1)
	count+=(a*2+b)//2
	print (count)


