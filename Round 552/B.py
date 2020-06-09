n=int(input())
l=list(map(int,input().split()))
l1=list(set(l))
l=sorted(l)
l1=sorted(l1)
x=-1
y=-1
if len(l1)==1:
	print (0)
elif len(l1)==2:
	x=l[-1]-l[0]
	y=(l[-1]+l[0])/2
	if int(y)==y:
		print (int(min(x,y-l[0])))
	else:
		print (x)
elif len(l1)==3:
	a=l1[0]
	b=l1[1]
	c=l1[2]
	if c-b==b-a:
		x=c-b
	if x==-1:
		print (-1)
	else:
		print (x)
else:
	print (-1)


