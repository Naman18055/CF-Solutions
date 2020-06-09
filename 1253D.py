import sys
input = sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
graph=[[] for i in range(n)]
for i in range(m):
	a,b=map(int,input().split())
	graph[a-1].append(b-1)
	graph[b-1].append(a-1)

vis=[0]*n
m=-1
ans=0
for i in range(n):
	if not vis[i]:
		if i<m:
			ans+=1
		queue=[i]
		queue=deque(queue)
		while len(queue)!=0:
			e=queue.popleft()
			m=max(e,m)
			vis[e]=1
			for i in graph[e]:
				if not vis[i]:
					queue.append(i)
					vis[i]=1
print (ans)