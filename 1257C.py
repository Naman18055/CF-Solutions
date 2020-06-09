for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	if len(set(l))==n:
		print (-1)
		continue
	d={}
	for i in range(n):
		if l[i] not in d:
			d[l[i]]=[i]
		else:
			d[l[i]].append(i)
	ans=n
	for i in d:
		for j in range(1,len(d[i])):
			ans=min(ans,d[i][j]-d[i][j-1]+1)
	print (ans)