for nt in range(int(input())):
	n,m=map(int,input().split())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	d={}
	time=0
	for i in range(n):
		if a[i]!=b[0]:
			d[str(a[i])]=1
		else:
			time+=2*i+1
			loc=i
			break
	for i in range(1,m):
		if str(b[i]) in d:
			time+=1
		else:
			for j in range(loc+1,n):
				if a[j]==b[i]:
					time+=(2*(j-i)+1)
					loc=j
					break
				else:
					d[str(a[j])]=1
		#print (d,time,loc,b[i])
	print (time)