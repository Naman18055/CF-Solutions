t=int(input())
for nt in range(t):
	n=int(input())
	num=input()
	f=num.find("8")
	if f==-1:
		print ('NO')
	else:
		if len(num[f:])>=11:
			print ("YES")
		else:
			print ("NO")