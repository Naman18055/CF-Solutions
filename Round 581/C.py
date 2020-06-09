import sys
from collections import deque
input = sys.stdin.readline

def bfs(root,l):
	q=[root]
	q=deque(q)
	j=1
	ans=[root]
	while j<len(l):
		element = q.popleft()
		#visited[element]=1
		if len(graph[element])==1:
			q.append(l[j]-1)
			j+=1
		else:
			ans.append(l[j]-1)
			q.append(l[j]-1)
			j+=1
	#ans.append(l[-1]-1)
	if ans[-1]!=l[-1]-1:
		ans.append(l[-1]-1)
	return ans


n=int(input())
graph=[[] for i in range(n)]
for i in range(n):
	a=input()
	for j in range(n):
		if a[j]=="1":
			graph[int(i)].append(int(j))
			#graph[int(j)].append(int(i))
m=int(input())
l=list(map(int,input().split()))
print (graph)
temp=bfs(l[0]-1,l)
print (len(temp))
print (*temp)