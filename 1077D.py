from collections import Counter

def check(num):
	count=0
	for i in freq:
		count+=i[0]//num
	if count>=k:
		return True
	return False

n,k=map(int,input().split())
l=list(map(int,input().split()))
c=Counter(l)
freq=[]
for i in c:
	freq.append((c[i],i))
freq.sort(reverse=True)
low=1
high=10**6
while (low<high):
	mid=(low+high)//2
	if check(mid):
		low=mid+1
	else:
		high=mid-1
if check(low):
	low = low
else:
	low = low-1
ans=[]
# print (low)
for i in freq:
	for j in range(max(1,i[0]//low)):
		ans.append(i[1])
		if len(ans)==k:
			break
	if len(ans)==k:
		break
# if n==163663:
	# print (low)
print (*ans)
