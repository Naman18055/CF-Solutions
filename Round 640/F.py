import math
for nt in range(int(input())):
	a,b,c=map(int,input().split())
	ans=""
	if b!=0:
		if a!=0:
			
			if b%2:
				ans="0"*(a)
				ans+="01"*((b+1)//2)
				ans+="1"*c
			else:
				ans="0"*(a+1)
				ans+="10"*((b+1)//2)
				
			print (ans)
		else:
			if b%2:
				ans+="01"*((b+1)//2)
				ans+="1"*c
				print (ans)
			else:
				ans+="10"*((b+1)//2)
				ans+="1"*(c+1)
				print (ans)
	else:
		if a==0:
			print ("1"*(c+1))
		else:
			print ("0"*(a+1))