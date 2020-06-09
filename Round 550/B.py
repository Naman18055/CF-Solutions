n=int(input())
l=list(map(int,input().split()))
o,e=0,0
ol,el=[],[]
for i in l:
	if i%2==0:
		e+=1
		el.append(i)
	else:
		o+=1
		ol.append(i)
if abs(o-e)<=1:
	print (0)
else:
	if o>e:
		a=o-e-1
		ol=sorted(ol)
		print (sum(ol[-a:]))
	else:
		a=e-o-1
		el=sorted(el)
		print (sum(el[-a:]))