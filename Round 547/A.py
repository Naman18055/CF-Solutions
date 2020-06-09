def f(x):
	global count
	if x==1:
		return True
	else:
		if x%2==0:
			count+=1
			return f(x//2)
		elif x%3==0:
			count+=1
			return f(x//3)
		else:
			return False

n,m=map(int,input().split())
x=m/n
if int(x)!=x:
	print (-1)
else:
	count=0
	if f(x):
		print (count)
	else:
		print (-1)
