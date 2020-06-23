import math
import sys
input = sys.stdin.buffer.readline
n,m,p=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
f,s = -1,-1
for i in range(m):
	if b[i]%p!=0 and f==-1:
		f = i
for i in range(n):
	if a[i]%p!=0 and s==-1:
		s = i
print (f+s)