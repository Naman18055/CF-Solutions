def find(n):
	low=0
	high=len(l)-1
	while low<high:
		mid=(low+high)//2
		if l[mid]>n:
			high=mid-1
		elif l[mid]<n:
			low=mid+1
		else:
			return n
	if l[low]>n:
		return l[low-1]
	else:
		return l[low]

l=[2]
for i in range(1,100000):
	l.append((i+1)*2+(3*((i+1)*i)//2))
# print (l[-1])
for nt in range(int(input())):
	n=int(input())
	count=0
	while n>1:
		n-=find(n)
		count+=1
	print (count)