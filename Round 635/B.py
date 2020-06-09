for nt in range(int(input())):
	x,n,m=map(int,input().split())
	if x<=10*m:
		print ("YES")
		continue
	if n==0:
		print ("NO")
		continue
	# if m==1:
	# 	if x!=11:
	# 		print ("NO")
	# 	else:
	# 		print ("YES")
	# 	continue
	# flag=1
	ans="YES"
	while True:
		if n!=0:
			x=x//2+10
			n-=1
		if n==0 and x>10*m:
			ans="NO"
			break
		elif n==0:
			break

		# print (x,n)

	print (ans)
