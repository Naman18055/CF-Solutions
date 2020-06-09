for nt in range(int(input())):
	n,m = map(int,input().split())
	f = list(map(int,input().split()))
	if n==2:
		print (-1)
		continue
	a = sorted(f)
	if n==m:
		print (2*sum(a))
		for i in range(1,n):
			print (i,i+1)
		print (n,1)
		continue
	if n>m:
		print (-1)
		continue
	print (2*sum(a)*((a[0]+a[1])*(m-n)))
	for i in range(1,n):
		print (i,i+1)
	print (n,1)
	x1,x2 = f.index(a[0]),f.index(a[1])
	for i in range(m-n):
		print (x1+1,x2+1)
