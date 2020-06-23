for nt in range(int(input())):
	n,x,y = map(int,input().split())
	minn = max(1,min(n,(x+y)-(n+1)+2))
	if (x+y)>=n+1:
		maxx = n
		print (minn,maxx)
		continue
	print (minn,min(n,x+y-1))