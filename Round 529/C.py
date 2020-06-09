n,k=(map(int,input().split()))
n=bin(n)[2:]
if n.count("1")>k:
	print ("NO")
else:
	l=[]
	for i in range(len(n)):
		if n[i]=="1":
			l.append(2**(len(n)-i-1))
	l.sort(reverse=True)
	j=0
	while k-len(l)>0:
		# if l[-1]==1:
		# 	print ("NO")
		# 	exit(0)
		while j<(len(l)) and l[j]==1:
			j=j+1
		if j>=(len(l)):
			print ("NO")
			exit(0)
		l[j]=l[j]//2
		l.append(l[j])
	l.sort()
	print ("YES")
	for i in l:
		print (i,end=" ")
