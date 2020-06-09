n,m=map(int,input().split())
n,m=min(n,m),max(n,m)
count=0
if True:
	if n%3==1:
		count+=(((m+1)//2)*(n//3))
		if m%3==2:
			count+=(m//3+1)
		else:
			count+=(m//3)
	elif n%3==2:
		count+=(((m+1)//2)*(n//3+1))
	else:
		count+=(((m+1)//2)*(n//3))
	count1=count
count=0
if True:
	n,m=m,n
	if n%3==1:
		count+=(((m+1)//2)*(n//3))
		if m%3==2:
			count+=(m//3+1)
		else:
			count+=(m//3)
	elif n%3==2:
		count+=(((m+1)//2)*(n//3+1))
	else:
		count+=(((m+1)//2)*(n//3))
	count2=count
count=0
if True:
	if n%3==1:
		count+=(((m+1)//2)*(n//3))
		if m%3==2:
			count+=(m//3+1)
		else:
			count+=(m//3)
	elif n%3==2:
		count+=(((m+1)//2)*(n//3+1))
	else:
		count+=(((m+1)//2)*(n//3))
	count3=count
print (max(count1,count2,count3))





