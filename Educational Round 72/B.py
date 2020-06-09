import math
t=int(input())
for nt in range(t):
	n,x=map(int,input().split())
	l=[]
	m=-1
	ma=-1
	mb=-1
	left=x
	for i in range(n):
		a,b=map(int,input().split())
		if a-b>m:
			m=a-b
		if a>ma:
			ma=a
		# if b>mb:
		# 	mb=b
		l.append([a,b])
	if m>0:
		count=0
		if ma>=x:
			print (1)
		else:
			left=x-ma
			print (math.ceil(left/m)+1)
	elif m==0:
		if ma>=x:
			print (1)
		else:
			print (-1)
	else:
		print (-1)


