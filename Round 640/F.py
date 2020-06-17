import math
for nt in range(int(input())):
	a,b,c=map(int,input().split())
	ans=""
	if b!=0:
		ans = "10"*((b+1)//2)
		ans += "1"*(1-b%2)
		ans = "1"*(c)+ans[0]+"0"*(a)+ans[1:]
		print (ans)
	else:
		if a==0:
			print ("1"*(c+1))
		else:
			print ("0"*(a+1))