n=int(input())
l=list(map(int,input().split()))
l.sort()
if n==1:
	print ('YES')
	print (l[0])
elif n==2:
	if l[0]==l[-1]:
		print ('YES')
		print (l[0],l[0])
		print (l[0],l[0])
elif n%2==1:
	i=0
	ans=0
	index=-1
	while i<len(l) and ans!=2:
		if ans==0:
			if l[i]!=l[i+1]:
				ans=1
				index=i
				i=i+1
			elif l[i]==l[i+1] and l[i+1]==l[i+2] and l[i+2]==l[i+3]:
				i=i+4
			else:
				ans=2
		elif ans==1:
			if l[i]==l[i+1] and l[i+1]==l[i+2] and l[i+2]==l[i+3]:
				i=i+4
			else:
				ans=2
	if ans==2:
		print ('NO')
	else:
		if index>=0:
			element = l.pop(index)
			




