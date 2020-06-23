import math
n,l,r=map(int,input().split())
if n==0:
	print (0)
	exit(0)
elif n==1:
	print (1)
	exit(0)
elif n==2:
	ans=[1,0,1]
	print (ans[l-1:r].count(1))
	exit(0)
elif n==3:
	ans=[1,1,1]
	print (ans[l-1:r].count(1))
	exit(0)
m=n
if n<100000:
	a=[]
	while n>1:
		a.append(n%2)
		n=n//2
	ans=[]
	ans.extend([1,a[-1],1])
	# print (a)
	for i in range(len(a)-2,-1,-1):
		ans.append(a[i])
		ans.extend(ans[0:-1])
	count=0
	for i in range(l,r+1):
		if ans[i-1]==1:
			count+=1
	# print (ans)
	print (count)
	exit()
b=bin(n)[2:]
i=len(b)-1
d={}
while n>1:
	d[2**i]=n%2
	n=n//2
	i-=1

count=0
prev=2**(int(math.log(l,2)))
# print (d)
for i in range(l,r+1):
	if i in d:
		if d[i]==1:
			# print (i)
			count+=1
		prev=i
	else:
		k=i
		j=prev
		while k not in d and k!=1:
			if j<k:
				k=j-(k-j)
			j=j//2
		if k==1:
			# print (i,k)
			count+=1
		else:
			if d[k]==1:
				# print (i,k)
				count+=1
print (count)
