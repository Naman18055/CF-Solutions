mod=998244353
from collections import defaultdict
import sys
input = sys.stdin.readline
n=int(input())
s1=[]
s2=[]
d={}
for i in range(n):
	temp=(list(map(int,input().split())))
	s1.append([temp[0],temp[1]])
	s2.append([temp[0],temp[1]])
	if (temp[0],temp[1]) in d:
		d[(temp[0],temp[1])]+=1
	else:
		d[(temp[0],temp[1])]=1
s1.sort(key = lambda x:x[0])
s2.sort(key = lambda x:x[1])
l1=[]
l2=[]
factorial=[1,1]
for i in range(2,n+1):
	factorial.append(((factorial[-1]*i)%998244353))
count=1
similar=1
for i in d:
	similar=similar*factorial[d[i]]
for i in range(n-1):
	if s1[i][0]==s1[i+1][0]:
		count+=1
	else:
		l1.append(count)
		count=1
l1.append(count)
count=1
for i in range(n-1):
	if s2[i][1]==s2[i+1][1]:
		count+=1
	else:
		l2.append(count)
		count=1
l2.append(count)
if len(l1)==1 or len(l2)==1:
	print (0)
	exit(0)
subtract=0
calc=1
for i in l1:
	calc=(calc*factorial[i])%998244353
subtract+=calc
calc=1
for i in l2:
	calc=(calc*factorial[i])%998244353
subtract+=calc
# s1.sort(key = lambda x:x[1])
flag=0
calc=0
for i in range(n-1):
	if s1[i+1][1]<s1[i][1]:
		flag=1
		break
# print (flag,similar,subtract,s1)
if flag==0:
	subtract=(subtract%mod-(similar%998244353))%998244353
subtract=subtract%998244353
print ((factorial[n]-subtract)%998244353)


