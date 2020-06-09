for nt in range(int(input())):
	n,x=map(int,input().split())
	l=list(map(int,input().split()))
	l.sort()
	vis=[-1]*100
	for i in range(n):
		vis[l[i]-1]=1
	i=0
	while x!=0 and i<100:
		# print (vis,x,i,vis[i])
		if vis[i]==-1:
			x=x-1
			vis[i]=1
		i+=1
		# print (vis,x,i,vis[i])
	# print (x)
	if x==0:
		# print (vis)
		if -1 in vis:
			for i in range(100):
				if vis[i]==-1:
					print (i)
					break
		else:
			print (100)
	else:
		print (100+x)