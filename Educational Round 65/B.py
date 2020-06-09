from collections import deque
def bfs(graph,start):
	q=[start]
	q=deque(q)
	traversed=[start]
	count=0
	visited=[0]*len(graph)
	visited[start]=1
	while len(q)!=0:
		element = q.popleft()
		for i in (graph[element]):
			if visited[i]==0:
				q.append(i)
				visited[i]=1
				count+=1
				traversed.append(i)
	for i in traversed:
		countall[i]=count+1


n,m=map(int,input().split())
graph=[[] for i in range(n)]
countall=[0]*n
for i in range(m):
	l=list(map(int,input().split()))
	temp=len(l)
	if temp>2:
		for j in range(temp):
			if j>1:
				graph[l[1]-1].append(l[j]-1)
				graph[l[j]-1].append(l[1]-1)
for i in range(n):
	if countall[i]==0:
		bfs(graph,i)
for i in countall:
	print (i,end=" ")
