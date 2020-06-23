n,s,k=map(int,input().split())
if s>k:
	print ("NO")
	exit()
ans=[]
curr=1
while k!=s and s!=0:
	if k-s+1>n-1:
		k-=n-1
		s-=1
		if curr==1:
			curr=n
		else:
			curr=1
		ans.append(curr)
	else:
		if curr==1:
			curr+=k-s+1
		else:
			curr-=(k-s+1)
		k-=(k-s+1)
		s-=1
		ans.append(curr)
	# print (k,s)
if s==0 and k>0:
	print ("NO")
else:
	if curr==1:
		for i in range(s):
			if curr==1:
				ans.append(2)
				curr=2
			else:
				ans.append(1)
				curr=1
	else:
		flag=False
		for i in range(s):
			if flag:
				ans.append(curr)
				flag=False
			else:
				ans.append(curr-1)
				flag=True
	print("YES")
	print (*ans)
