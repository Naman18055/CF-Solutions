def s(n):
	num=str(n)
	ans=1
	for i in num:
		ans=ans*(int(i))
	return ans

n=int(input())
m=s(n)
if n>10000:
	ones=int(str(n)[-1])
	n=n-(ones+1)
	temp=s(n)
	if temp>m:
		m=temp
	tens=int(str(n)[-2])
	n=n-(tens+1)*10
	temp=s(n)
	if temp>m:
		m=temp
	thou=int(str(n)[-3])
	n=n-(thou+1)*100
	temp=s(n)
	if temp>m:
		m=temp
	tent=int(str(n)[-4])
	n=n-(tent+1)*1000
	temp=s(n)
	if temp>m:
		m=temp
	for i in range(n,max(0,n-1000000000),-10000):
		temp=s(i)
		if temp>m:
			m=temp
	print (m)
else:
	for i in range(n,0,-1):
		temp=s(i)
		if temp>m:
			m=temp
	print (m)