for nt in range(int(input())):
	n,m=map(int,input().split())
	if n*m<=4:
		print ("YES")
		continue
	if n==1 or m==1:
		print ('YES')
		continue
	print ("NO")