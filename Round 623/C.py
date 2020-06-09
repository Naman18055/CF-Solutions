for nt in range(int(input())):
	n=int(input())
	b=list(map(int,input().split()))
	d=set(b)
	ansflag=0
	ans=[]
	d1={}
	for i in range(n):
		ans.append(b[i])
		k=1
		flag=0
		#print (ans)
		while True:
			if (b[i]+k)>2*n:
				flag=1
				break
			if b[i]+k not in d and b[i]+k not in d1:
				ans.append(b[i]+k)
				d1[b[i]+k]=1
				break
			else:
				k+=1
		if flag==1:
			print (-1)
			ansflag=1
			break
	if ansflag!=1:
		print (*ans)