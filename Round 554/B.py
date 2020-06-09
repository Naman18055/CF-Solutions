x=int(input())
b=bin(x)[2:]
if b.count("0")==0:
	print (0)
else:
	steps=0
	flag=0
	n=[]
	while True:
		b=bin(x)[2:]
		l=len(b)
		if b.count("0")==0:
			print (steps)
			for i in n:
				print (i,end=" ")
			break
		if flag==0:
			for i in range(l):
				if b[i]=="0":
					x=x^((2**(l-i))-1)
					n.append(l-i)
					steps+=1
					flag=1
					break
		elif flag==1:
			x=x+1
			steps+=1
			flag=0

