n=int(input())
fun=[1]
l=[]
s=1
for j in range(1,n//2+1):
	while s!=n+1:
		l.append(s)
		s=s+j
		if s>n:
			s=s-n
		if s==1:
			s=n+1
	if sum(l) not in fun:
		fun.append(sum(l))
	l=[]
	s=1
fun.sort()
for i in fun:
	print (i,end=' ')
