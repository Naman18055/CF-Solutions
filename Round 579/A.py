t=int(input())
for nt in range(t):
	n=int(input())
	l=list(map(int,input().split()))
	flag=0
	if n==1:
		print ("YES")
	else:
		findone=l.index(1)
		if l[(findone+1)%n]==2:
			clockwise=1
		elif l[findone-1]==2:
			clockwise=0
		else:
			clockwise=-1
		if clockwise==-1:
			print ("NO")
		elif clockwise==0:
			for i in range(findone-1,-1,-1):
				if l[i]!=l[i+1]+1:
					print ("NO")
					flag=1
					break
			if flag==0:
				for i in range(n-1,findone,-1):
					if l[i]!=(l[(i+1)%n])+1:
						print ("NO")
						flag=1
						break
			if flag==0:
				print ("YES")
		else:
			for i in range(findone+1,n):
				if l[i]!=l[i-1]+1:
					print ("NO")
					flag=1
					break	
			if flag==0:
				for i in range(findone):
					if l[i]!=(l[i-1])+1:
						print ("NO")
						flag=1
						break
			if flag==0:
				print ("YES")

					
