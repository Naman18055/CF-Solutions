for nt in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	if a==b:
		print ("YES")
		continue
	z=-1
	o=-1
	m=-1
	for i in range(n):
		if a[i]==0 and z==-1:
			z=i
		elif a[i]==1 and o==-1:
			o=i
		elif a[i]==-1 and m==-1:
			m=i
	ans="YES"
	for i in range(n-1,-1,-1):
		# print (z,o,m,i)
		x=b[i]-a[i]
		if x==0:
			continue
		if x<0:
			if m==-1 or m>=i:
				ans="NO"
				break
		if x>0:
			if o==-1 or o>=i:
				ans="NO"
				break
	print (ans)