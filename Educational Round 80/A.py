import math
for nt in range(int(input())):
	n,d=map(int,input().split())
	if d<=n:
		print ("YES")
	else:	
		flag=0
		for i in range(min(n,int(d**(0.5))+1)):
			if (i+math.ceil(d/(i+1)))<=n:
				print ("YES")
				flag=1
				break
		if flag==0:
			print ("NO")
