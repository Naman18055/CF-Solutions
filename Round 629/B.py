for nt in range(int(input())):
	n,k=map(int,input().split())
	for i in range(1,n+1):
		c=(i*(i+1))//2
		# print (k,c)
		if k<=c:
			pos1=i
			pos2=k-1-((i*(i-1))//2)
			break
	ans=""
	for i in range(n-1,-1,-1):
		if i==pos1 or i==pos2:
			ans+="b"
		else:
			ans+="a"
	print (ans)