def compute(y, x): 
	A = (y - x)//2
	a = 0
	b = 0
	for i in range(64): 
		Xi = (x & (1 << i)) 
		Ai = (A & (1 << i)) 
		if (Xi == 0 and Ai == 0): 
			pass
			
		elif (Xi == 0 and Ai > 0): 
			a = ((1 << i) | a) 
			b = ((1 << i) | b) 
		
		elif (Xi > 0 and Ai == 0): 
			a = ((1 << i) | a) 
		else:
			return [False,0,0]

	return [True,a,b] 

u,v=map(int,input().split())
if u==0 and v==0:
	print (0)
elif u==0 and v%2==0:
	print (2)
	print (v//2,v//2)
elif u>v:
	print (-1)
elif u==v:
	print (1)
	print (u)
else:
	if u%2!=v%2:
		print (-1)
		exit()
	# if u%2==1 and u==v:
	# 	print (2)
	# 	print (1,u-1)
	# 	exit()
	# elif u%2==0 and u==v:
	# 	if bin(u-2)[-2]=="1":
	# 		print (-1)
	# 		exit()
	# 	else:
	# 		print (2)
	# 		print (2,u-2)
	# 		exit()
	ans=compute(v, u)
	if ans[0]==True and ans[1]!=0 and ans[2]!=0:
		print (2)
		print (ans[1],ans[2])
	else:
		print (3)
		print (u,(v-u)//2,(v-u)//2)