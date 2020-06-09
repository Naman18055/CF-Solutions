for nt in range(int(input())):
	n,p,k=map(int,input().split())
	l=list(map(int,input().split()))
	l.sort()
	odd=[]
	even=[]
	for i in range(n):
		if i%2==0:
			odd.append(l[i])
		else:
			even.append(l[i])
	count=0
	total1=0
	for i in range(len(odd)):
		count+=odd[i]
		if count>p:
			break
		else:
			if i==0:
				total1+=1
			else:
				total1+=2
	count=0
	total2=0
	for i in range(len(even)):
		count+=even[i]
		if count>p:
			break
		else:
			total2+=2
	print (max(total1,total2))

