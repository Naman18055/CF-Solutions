t=int(input())
for i in range(t):
	m=0
	s1=''
	ln,lk=[],[]
	l=list(map(int,input().split()))
	n=l[0]
	k=l[1]
	for j in range(k):
		lk.append(j)
	for k in range(n):
		ln.append(k)
	while len(lk)<len(ln):
		lk.append(lk[m])
		m+=1
	for x in lk:
		s1+=chr(97+x)
	print (s1)



