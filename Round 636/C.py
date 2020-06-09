for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	ans=0
	if l[0]>0:
		pos=1
		m=l[0]
	else:
		pos=0
		m=l[0]
	for i in range(1,n):
		if l[i]>0 and pos:
			m=max(m,l[i])
		elif l[i]<0 and not pos:
			m=max(m,l[i])
		elif l[i]>0 and not pos:
			ans+=m
			m=l[i]
			pos=1
		else:
			ans+=m
			m=l[i]
			pos=0
	ans+=m
	print (ans)