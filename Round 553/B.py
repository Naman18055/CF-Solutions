n,m=map(int,input().split())
mat=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
	mat[i]=list(map(int,(input().split())))
xor=0
flag=0
row=0
for i in range(n):
	if mat[i].count(mat[i][0])==m:
		xor=xor^mat[i][0]
	else:
		flag=1
		row=i
		break
if flag==0:
	if xor>0:
		print ('TAK')
		for i in range(n):
			print (1,end=" ")
	else:
		print ('NIE')
else:
	xor1,xor2=0,0
	num1,num2=0,0
	for i in range(n):
		if i==row:
			temp=list(set(mat[i]))
			xor1=xor1^temp[0]
			num1=temp[0]
			xor2=xor2^temp[1]
			num2=temp[1]
		else:
			xor1=xor1^mat[i][0]
			xor2=xor2^mat[i][0]
	if xor1>0:
		print ('TAK')
		for i in range(n):
			if i==row:
				print (mat[i].index(num1)+1,end=" ")
			else:
				print (1,end=" ")
	elif xor2>0:
		print ("TAK")
		for i in range(n):
			if i==row:
				print (mat[i].index(num2)+1,end=" ")
			else:
				print (1,end=" ")
	else:
		print ('NIE')

