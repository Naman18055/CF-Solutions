def calc(n,r):
	if n<r:
		return 0
	return 1+calc(n//r,r)
for nt in range(int(input())):
	n,k=map(int,input().split())
	a=list(map(int,input().split()))
	d={}
	flag=0
	for i in a:
		temp=i

		while temp//k!=0:
			b=int(calc(temp,k))
			if b in d:
				flag=1
				break
			else:
				d[b]=1
			temp=temp-(k**b)
			#print (b,temp)
		if flag==1:
			break

		if temp>1:
			flag=1
			break
		elif temp==1:
			if 0 in d:
				flag=1
				break
			else:
				d[0]=1

	if flag==0:
		print ("YES")
	else:
		print ("NO")
