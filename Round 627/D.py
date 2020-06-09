def bs(new,k):
	low=0
	high=len(new)
	while low<high:
		mid=(low+high)//2
		if new[mid]<=k:
			low=mid+1
		elif new[mid]>k:
			high=mid-1
	if low!=len(new) and new[low]<=k:
		low+=1
	#print (low)
	return len(new)-low


n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
new=[]
temp=[]
for i in range(n):
	new.append(a[i]-b[i])
	temp.append((a[i],b[i]))
#print (new)
new.sort()
#print (new)
count=0
#print (new)
for i in range(n):
	temp=(bs(new,-1*new[i]))
	if n-temp<i:
		temp-=1
	count+=temp
print (count//2)