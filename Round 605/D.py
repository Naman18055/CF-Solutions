n=int(input())
l=list(map(int,input().split()))
sufinc=[1]*n
count=1
for i in range(n-2,-1,-1):
	if l[i]<l[i+1]:
		count+=1
		sufinc[i]=count
	else:
		count=1
		sufinc[i]=count
#print (sufinc)
preinc=[1]*n
count=1
for i in range(1,n):
	if l[i]>l[i-1]:
		count+=1
		preinc[i]=count
	else:
		count=1
		preinc[i]=count
#print (preinc)
ans=0
ans=max(sufinc[0],preinc[-1])
ans=max(sufinc[1],preinc[-2],ans)
for i in range(1,n-1):
	if l[i+1]>l[i-1]:
		if preinc[i-1]+sufinc[i+1]>ans:
			ans=preinc[i-1]+sufinc[i+1]
	else:
		ans = max(ans,preinc[i-1],sufinc[i+1])
# flag=0
# for i in range(1,n):
# 	if l[i]<=l[i-1]:
# 		flag=1
# 		break
# if flag==0:
# 	print (n)
# else:
# 	print (ans)
print (ans)