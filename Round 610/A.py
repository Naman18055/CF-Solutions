for nt in range(int(input())):
	a,b,c,r=map(int,input().split())
	ran=[c-r,c+r]
	# for i in range(c-r,c+r+1):
	# 	ran.append(i)
	ans=abs(b-a)
	if a>=c-r and a<=c+r:
		x=1
	else:
		x=0
	if b>=c-r and b<=c+r:
		y=1
	else:
		y=0
	if x==1 and y==1:
		print (0)
	elif x==1 and y==0:
		if b<=ran[0]:
			print (abs(b-ran[0]))
		else:
			print (abs(b-ran[-1]))
	elif x==0 and y==1:
		if a<=ran[0]:
			print (abs(a-ran[0]))
		else:
			print (abs(a-ran[-1]))
	else:
		if a<=ran[0] and b<=ran[0]:
			print (abs(b-a))
		elif a>=ran[-1] and b>=ran[-1]:
			print (abs(b-a))
		else:
			print (abs(b-a)-2*r)
