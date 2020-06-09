import math
from collections import defaultdict
n,k=map(int,input().split())
l=[]
d=defaultdict(int)
for i in range(n):
	temp=int(input())
	l.append(temp)
	d[temp]+=1
count=0
left=math.ceil(n/2)
for i in d:
	if d[i]%2==0:
		left-=(d[i]//2)
	else:
		count+=1
		left-=(d[i]//2)
print (min(n,n-(count-left)))

