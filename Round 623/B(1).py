for nt in range(int(input())):
	a,b,p=map(int,input().split())
	s=input()
	n=len(s)
	cost=[0]
	index=[1]
	for i in range(1,n):
		if s[i]!=s[i-1]:
			if s[i]=="A":
				cost.append(b+cost[-1])
				index.append(i+1)
			else:
				cost.append(a+cost[-1])
				index.append(i+1)
	if s[n-1]==s[n-2]:
		if s[n-1]=="A":
			cost.append(a+cost[-1])
			index.append(n)
		else:
			cost.append(b+cost[-1])
			index.append(n)
	#print (cost)
	#print (index)
	flag=0
	for i in range(len(cost)):
		if cost[-1]-cost[i]<=p:
			print (index[i])
			flag=1
			break
	if flag==0:
		print (n)
