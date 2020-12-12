import sys
import math
input = sys.stdin.buffer.readline
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a


n=int(input())
a=I()
b=I()
f=True		
done=False
ac=a.count(1)
bc=b.count(1)
both=0
for i in range(n):
	if (a[i]==0 and b[i]==1) or (a[i]==0 and b[i]==1):f=False
	if a[i] and b[i]:both+=1
if ac==both:print(-1)
else:
	print(math.ceil((bc-both+1)/(ac-both)))





