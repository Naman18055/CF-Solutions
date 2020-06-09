n=int(input())
for i in range(n):
	s=input()
	l=[]
	ans=1
	for j in s:
		a=ord(j)
		l.append(a)
	l=sorted(l)
	#print (l)
	for j in range(1,len(l)):
		if l[j]-1!=l[j-1]:
			print ("No")
			ans=0
			break
	if ans==1:
		print ("Yes")