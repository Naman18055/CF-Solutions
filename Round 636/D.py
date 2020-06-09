for nt in range(int(input())):
	n,k=map(int,input().split())
	l=list(map(int,input().split()))
	s=[]
	d={}
	for i in range(n//2):
		a=l[i]+l[n-i-1]
		s.append((a,i))
		if a in d:
			d[a]+=1
		else:
			d[a]=1
	s.sort()
	if s[0][0]==s[-1][0]:
		print (0)
		continue
	r=[]
	start={}
	end={}
	for i in range(n//2):
		m1=max(l[i],l[n-i-1])
		m2=min(l[i],l[n-i-1])
		if m2+1 in start:
			start[m2+1]+=1
		else:
			start[m2+1]=1
		if m1+k in end:
			end[m1+k]+=1
		else:
			end[m1+k]=1
		# r.append((m2+1,m1+k))

	if 2 not in start:
		start[2]=0
	if 2 not in end:
		end[2]=0
	for i in range(3,2*k+1):
		if i not in start:
			start[i]=start[i-1]
		else:
			start[i]+=start[i-1]
		if i not in end:
			end[i]=end[i-1]
		else:
			end[i]+=end[i-1]
	ans=0
	# print (start,end)
	if 2 in d:
		ans=2*(n//2-start[2])-d[2]+start[2]
	else:
		ans=2*(n//2-start[2])+start[2]
	for i in range(3,2*k+1):
		# print (i,n//2-start[i]+end[i-1])
		if i in d:
			ans=min(ans,2*(n//2-start[i]+end[i-1])-d[i]+start[i]-end[i-1])
		else:
			ans=min(ans,2*(n//2-start[i]+end[i-1])+start[i]-end[i-1])
	print (ans)