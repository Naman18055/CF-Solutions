import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def bs(num):
	low=0
	high=k-1
	while (low<high):
		mid=(low+high)//2
		if l[mid]>num:
			high=mid-1
		else:
			low=mid+1
	if l[low]>num:
		return low
	else:
		return low+1

def solve(start,end):
	if start==end:
		if start in d:
			return 1*b*d[start]
		else:
			return a
	else:
		if start!=0:
			count = bs(end)-bs(start-1)
		else:
			count = bs(end)

		if count==0:
			return a
		else:
			temp1=solve(start,(start+end)//2)
			temp2=solve((start+end)//2+1,end)
			return min(temp1+temp2,b*count*(end-start+1))
		# print (start,end,temp1,temp2,find(start,end))
		# return min(temp1+temp2,find(start,end))

n,k,a,b=map(int,input().split())
l=list(map(int,input().split()))
for i in range(k):
	l[i]-=1
l.sort()
d={}
for i in l:
	if i in d:
		d[i]+=1
	else:
		d[i]=1
print (solve(0,2**n-1))