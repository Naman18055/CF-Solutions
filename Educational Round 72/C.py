t=int(input())
for nt in range(t):
	s=input()
	n=len(s)
	count=s.count("1")-1
	for i in range(2,n//2+1):
		b=bin(i)[2:]
		x=len(b)
		b="0"*(i-x)+b
		find=-1
		flag=0
		#print (b,s)
		#print (b,count)
		while find!=-1 or flag==0:
			flag=1
			count+=1
			find=s.find(b,find+len(b),n)
	#print (count)
	for i in range(n//2+1,n):
		b=bin(i)[2:]
		x=len(b)
		b="0"*(i-x)+b
		if b in s:
			count+=1
	print (count)
