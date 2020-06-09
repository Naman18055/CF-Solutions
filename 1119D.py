import sys
input = sys.stdin.readline

def bs(num):
	low=0
	high=len(diff)-1
	while (low<high):
		mid=(low+high)//2
		if diff[mid]<=num:
			low=mid+1
		else:
			high=mid-1
	if diff[low]<=num:
		return len(diff)-low-1
	else:
		return len(diff)-low

int(input())
s=sorted(list(set(map(int,input().split()))))
n=len(s)
diff=[]
for i in range(1,n):
	diff.append(s[i]-s[i-1])
diff.sort()
if n==1:
	for i in range(int(input())):
		l,r=map(int,input().split())
		print (r-l+1,end=" ")
	exit()

suff=[diff[-1]]
for i in range(len(diff)-2,-1,-1):
	suff.append(suff[-1]+diff[i])
# print (s)
# print (diff)
# print (suff)
minn,maxx=min(s),max(s)
for i in range(int(input())):
	l,r=map(int,input().split())
	count=bs(r-l+1)
	# print (count)
	if count==0:
		print (maxx+r-minn-l+1,end=" ")
	else:
		print (maxx+r-minn-l+1-(suff[count-1]-count*(r-l+1)),end=" ")
print ()