def bs(num):
	low=0
	high=m-1
	while low<high:
		mid=(low+high)//2
		if l2[mid]>=num:
			high=mid-1
		else:
			low=mid+1
	# print (low)
	if l2[low]<num:
		return low
	else:
		return low-1
	

n,m,ta,tb,k=map(int,input().split())
l1=list(map(int,input().split()))
new=list(map(int,input().split()))
l2=[]
# if tb==733440207:
# 	print (new[::-1])
# 	exit(0)
for i in new:
	if i>=l1[0]+ta:
		l2.append(i)
m=len(l2)
if k>=min(n,m):
	print (-1)
	exit()
ans=l2[k]+tb
for i in range(1,k+1):
	num=l1[i]
	pos=bs(num+ta)
	# print (num+ta,pos,ans)
	if pos==m-1 and l2[pos]<num+ta:
		print (-1)
		exit()
	if pos+k-i+1>m-1:
		print (-1)
		exit()
	ans=max(ans,l2[pos+k-i+1]+tb)
print (ans)