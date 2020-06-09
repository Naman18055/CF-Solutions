def check(num):
	arr=[[] for i in range(num)]
	j,count=0,0
	for i in range(n):
		arr[j].append(max(0,c[i]-len(arr[j])))
		count+=arr[j][-1]
		j=(j+1)%num
	if count>=m:
		return True
	return False

n,m=map(int,input().split())
c=list(map(int,input().split()))
c.sort(reverse=True)
# print (c)
if sum(c)<m:
	print (-1)
	exit()
low=1
high=n
while (low<high):
	mid=(low+high)//2
	if check(mid):
		high=mid-1
	else:
		low=mid+1
if check(low):
	print (low)
else:
	print (low+1)