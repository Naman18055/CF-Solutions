for nt in range(int(input())):
	n=int(input())
	new=list(map(int,input().split()))
	s=sum(new)
	count=0
	start=-1
	for i in range(len(new)):
		if new[i]>=0:
			start=i
			break
	if start==-1:
		print ("NO")
		continue
	if start!=0:
		flag1=1
	else:
		flag1=0
	flag=0
	for i in range(start,n):
		if count+new[i]>0:
			count+=new[i]
		else:
			count=0
			flag1=1
		if count>=s and (flag1==1 or i!=n-1):
			print ("NO")
			flag=1
			break
		#print (s,count)
	if flag==0:
		print ("YES")