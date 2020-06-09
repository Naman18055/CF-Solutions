t=int(input())
l=[]
for i in range(1,10):
	for j in range(1,10):
		l.append(str(i)*j)
#print (l)
for nt in range(t):
	n=int(input())
	count=0
	for i in l:
		if int(i)<=n:
			count+=1
	print (count)
