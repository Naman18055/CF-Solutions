from collections import deque
import sys
def levels(start):
	count=0
	flag=0
	l=[start,-1]
	l=deque(l)
	while l.count(-1)!=len(l):
		element=l.popleft()
		if element==-1:
			count+=1
			l.append(-1)
		else:
			for i in parent[element]:
				l.append(i)
	return count+1
input=sys.stdin.readline
n=int(input())
parent=[[] for i in range(n)]
root=[]
for i in range(n):
	p=int(input())
	if p!=-1:
		parent[p-1].append(i)
	else:
		root.append(i)
m=0
for i in root:
	temp=levels(i)
	if m<temp:
		m=temp
print (m)