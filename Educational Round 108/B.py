for nt in range(int(input())):
	n, m, k = map(int,input().split())
	if n==m:
		if k==((n-1)+(n*(n-1))):
			print ("YES")
		else:
			print ("NO")
		continue

	if n>m:
		minn = (m-1 + (m*(n-1)))
		maxx = (n-1 + (n*(m-1)))
	else:
		minn = (n-1 + (n*(m-1)))
		maxx = (m-1 + (m*(n-1)))

	if k>=minn and k<=maxx:
		print ("YES")
	else:
		print ("NO")

