for nt in range(int(input())):
	n,x=map(int,input().split())
	a=list(map(int,input().split()))
	o=0
	e=0
	for i in a:
		if i%2:
			o+=1
		else:
			e+=1
	if e==0 and x%2==0:
		print ("NO")
		continue
	if o==0:
		print ("NO")
		continue
	if o%2:
		print ("YES")
	else:
		if x<=n-1:
			print ("YES")
		else:
			print ("NO")
