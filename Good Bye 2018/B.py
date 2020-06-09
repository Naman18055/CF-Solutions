n=int(input())
l1,l2,l3,l4,l5=[],[],[],[],[]
y=0
ans=0
for i in range(n):
	l=list(map(int,input().split()))
	l1.append((l[0],l[1]))
for i in range(n):
	l=list(map(int,input().split()))
	l2.append((l[0],l[1]))
for j in l2:
	l3.append((l1[0][0]+j[0],l1[0][1]+j[1]))
if len(l1)>1:
	for j in l2:
		l5.append((l1[1][0]+j[0],l1[1][1]+j[1]))
for i in l3:
	for j in l5:
		if i==j:
			l4.append(i)
if len(l4)>0:
	ans=l4[-1]
else:
	ans=l3[-1]
if len(l1)>0:
	x=l1.pop(0)
if len(l1)>0:
	x=l1.pop(0)
for i in l1:
	for j in l2:
		if (i[0]+j[0],i[1]+j[1]) in l4:
			l4.append((i[0]+j[0],i[1]+j[1]))
			if len(l4)>2:
				if l4[-1]==l4[-2]:
					if l4[-1]==l4[-3]:
						ans=l4[-1]
						y=1
						break
	if y==1:
		break
for i in ans:
	print (i,end=' ')