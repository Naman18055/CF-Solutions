from collections import defaultdict
import math
n,k=map(int,input().split())
l=list(map(int,input().split()))
d=defaultdict(int)
for i in l:
	d[i%k]+=1
count=0
count+=(d[0]//2)*2
for i in range(1,math.ceil(k//2)+1):
	if i!=k-i:
		count+=(min(d[i],d[k-i])*2)
	else:
		count+=(d[i]//2)*2
print (count)