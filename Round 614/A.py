for nt in range(int(input())):
	n,s,k=map(int,input().split())
	l=list(map(int,input().split()))
	l.sort()
	if s not in l:
		print (0)
		continue
	else:
		ind=l.index(s)
		if l[-1]==n:
			ans1=10000000000000000
		else:
			ans1=l[-1]+1
		for i in range(ind+1,k):
			if l[i]!=l[i-1]+1:
				ans1=l[i-1]+1
				break
		if l[0]==1:
			ans2=10000000000000000
		else:
			ans2=l[0]-1
		for i in range(ind-1,-1,-1):
			if l[i]!=l[i+1]-1:
				ans2=l[i+1]-1
				break
		#print (ans1,ans2)
		print (min(abs(ans2-s),abs(ans1-s)))