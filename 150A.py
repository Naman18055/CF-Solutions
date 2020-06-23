q = int(input()) 
x = q
p = []
for i in range(2,int(q**0.5)+1):
	while q%i==0:
		p.append((i,q//i))
		q = q//i
if len(p)<=0:
	print (1)
	print (0)
	exit()
elif len(p)==1:
	print (2)
	exit()
if len(p)>2:
	print (1)
	print (p[0][0]*p[1][0])
	exit()
if p[0][0]*p[1][0]!=x:
	print (1)
	print (p[0][0]*p[1][0])
else:
	print (2)