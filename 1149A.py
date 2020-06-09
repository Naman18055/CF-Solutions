n=int(input())
l=list(map(int,input().split()))
one=l.count(1)
two=n-one
ans=[]
if one==0:
	for i in l:
		print (i,end=" ")
elif two==0:
	for i in l:
		print (i,end=" ")
else:
	ans.append(2)
	two-=1
	if one%2==0:
		while one!=1:
			ans.append(1)
			one-=1
		while two!=0:
			ans.append(2)
			two-=1
		ans.append(one)
	else:
		while one!=0:
			ans.append(1)
			one-=1
		while two!=0:
			ans.append(2)
			two-=1
	for i in ans:
		print (i,end=" ")