t=int(input())
for nt in range(t):
	h,n=map(int,input().split())
	string = ""
	l=list(map(int,input().split()))
	ans=0
	curr=h
	i=1
	while curr!=0:
		#print (curr,i)
		if i>=n:
			break
		if l[i]==1:
			break
		if l[i]==curr-1 and l[(i+1)%n]==curr-2:
			curr=curr-2
			i+=2
		elif l[i]==curr-1 and l[(i+1)%n]!=curr-2:
			#print (curr,i,ans)
			if i+1<n:
				ans+=1
				curr=l[i+1]+1
				i+=1
			else:
				ans+=1
				i+=1
				curr=curr-2
		else:
			curr=l[i]+1
	print (ans)
