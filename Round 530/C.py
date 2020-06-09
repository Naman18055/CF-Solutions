n=input()
k=int(input())
ans=''
x=n.count("*")+n.count("?")
w=len(n)-x
if len(n)-2*x>k:
	print ("Impossible")
elif (len(n)-x)==k:
	while n.find("?")!=-1:
		z=n.find("?")
		n=n[0:z]+n[z+1:]
	while n.find("*")!=-1:
		z=n.find("*")
		n=n[0:z]+n[z+1:]
	print (n)
elif (len(n)-2*x)==k:
	while n.find("?")!=-1:
		z=n.find("?")
		n=n[0:z-1]+n[z+1:]
	while n.find("*")!=-1:
		z=n.find("*")
		n=n[0:z-1]+n[z+1:]
	print (n)
else:
	if n.find("*")==-1:
		if n.find("?")==-1 and len(n)!=k:
			print ("Impossible")
		elif n.find("?")==-1 and len(n)==k:
			print (n)
		elif k>len(n)-x:
			print ('Impossible')
		else:
			v=w-k
			for i in range(v):
				z=n.find("?")
				n=n[0:z-1]+n[z+1:]
			while n.find("?")!=-1:
				z=n.find("?")
				n=n[0:z]+n[z+1:]
			print (n)
	elif n.find("?")==-1:
		if n.find("*")==-1 and len(n)!=k:
			print ("Impossible")
		elif n.find("*")==-1 and len(n)==k:
			print (n)
		else:
			u=n.count("*")-1
			for i in range(u):
				z=n.find("*")
				n=n[0:z-1]+n[z+1:]
			u=n.find("*")
			print (n[0:u]+(n[u-1:u])*(k-len(n)+1)+n[u+1:])
	else:
		while n.find("?")!=-1:
			z=n.find("?")
			n=n[0:z-1]+n[z+1:]
		u=n.count("*")-1
		for i in range(u):
			z=n.find("*")
			n=n[0:z-1]+n[z+1:]
		u=n.find("*")
		print (n[0:u]+(n[u-1:u])*(k-len(n)+1)+n[u+1:])



