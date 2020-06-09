for nt in range(int(input())):
	n,x=map(int,input().split())
	l=list(map(int,input().split()))
	s=0
	for i in range(n):
		if l[i]>=x:
			s+=(l[i]-x)
	l.sort(reverse=True)
	ans=0
	# print (s)
	for i in range(n):
		# print (s,l)
		if l[i]>=x:
			ans+=1
		else:
			a=min(s,x-l[i])
			s-=a
			l[i]+=a
			if l[i]>=x:
				ans+=1
	print(ans)
