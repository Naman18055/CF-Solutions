import sys
n,k=map(int,input().split())
if k==1:
	print ("!",1)
	sys.stdout.flush()
elif k<=(n+1)//2:
	a=[-1]*n
	d={}
	num=[]
	positions=[]
	print ("?",end=" ")
	for i in range(k):
		print (i+1,end=" ")
	print ()
	sys.stdout.flush()
	pos,apos=map(int,input().split())
	d[str(pos)]=1
	a[pos-1]=apos
	for j in range(k-1):
		tobe=[]
		for i in range(n):
			if str(i+1) not in d:
				tobe.append(i+1)
			if len(tobe)==k:
				break
		print ("?",end=" ")
		print (*tobe)
		sys.stdout.flush()
		pos,apos=map(int,input().split())
		d[str(pos)]=1
		a[pos-1]=apos
	print ("?",end=" ")
	new=[]
	for i in range(n):
		if a[i]!=-1:
			print (i+1,end=" ")
			new.append(a[i])
	print ()
	sys.stdout.flush()
	pos,apos=map(int,input().split())
	new.sort()
	print ("!",new.index(apos)+1)
elif k==n-1:
	below=0
	above=0
	positions=[]
	num=[]
	for i in range(n):
		tobe=[]
		print ("?",end=" ")
		for j in range(n):
			if j!=i:
				tobe.append(j+1)
			if len(tobe)==k:
				break
		print (*tobe)
		sys.stdout.flush()
		pos,apos=map(int,input().split())
		if len(num)==0:
			positions.append(pos)
			num.append(apos)
		else:
			if apos>num[-1] and pos!=i-1:
				above+=1
			elif apos<num[-1] and pos!=i-1:
				below+=1
			positions.append(pos)
			num.append(apos)
	print ("!",end=" ")
	if below==0 and above>=1:
		print (1)
	elif above==0:
		print (k)
	else:
		print (below+1)
else:
	tobe=[]
	d=[]
	below,above=0,0
	num=[]
	print ("?",end=" ")
	for i in range(k):
		tobe.append(i+1)
		d.append(i+1)
	print (*tobe)
	sys.stdout.flush()
	pos,apos=map(int,input().split())
	start=pos
	num.append(apos)
	for i in range(k):
		flag=0
		tobe=[]
		for j in range(n-1):
			if j+1!=start and j+1==d[i]:
				continue
			else:
				tobe.append(j+1)
			if len(tobe)==k:
				break
		print("?",end=" ")
		print (*tobe)
		sys.stdout.flush()
		pos,apos=map(int,input().split())
		if apos>num[-1]:
			above+=1
		elif apos<num[-1]:
			below+=1
		num.append(apos)
	print ("!",end=" ")
	if below==0 and above>=1:
		print (1)
	elif above==0:
		print (k)
	else:
		print (below+1)







