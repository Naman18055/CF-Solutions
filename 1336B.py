def find(arr,flag,num):
	if flag:
		low=0
		high=len(arr)-1
		while low<high:
			mid=(low+high)//2
			if arr[mid]<num:
				low=mid+1
			else:
				high=mid-1
		if arr[low]<num:
			if low!=len(arr)-1:
				return arr[low+1]
			else:
				return 10**20
		else:
			return arr[low]
	else:
		low=0
		high=len(arr)-1
		while low<high:
			mid=(low+high)//2
			if arr[mid]<num:
				low=mid+1
			else:
				high=mid-1
		if arr[low]>num:
			if low!=0:
				return arr[low-1]
			else:
				return 10**20
		else:
			return arr[low]


def solve(a,b,c):
	ans=10**20
	for i in b:
		x=find(a,0,i)
		y=find(c,1,i)
		ans=min(ans,(i-x)**2+(i-y)**2+(x-y)**2)
	return ans

for nt in range(int(input())):
	n1,n2,n3=map(int,input().split())
	l1=sorted(list(map(int,input().split())))
	l2=sorted(list(map(int,input().split())))
	l3=sorted(list(map(int,input().split())))
	ans=solve(l1,l2,l3)
	ans=min(ans,solve(l1,l3,l2))
	ans=min(ans,solve(l2,l1,l3))
	ans=min(ans,solve(l2,l3,l1))
	ans=min(ans,solve(l3,l1,l2))
	print (min(ans,solve(l3,l2,l1)))