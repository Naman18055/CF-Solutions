from collections import deque

def bfs(root,graph):
	visited = [0]*n
	visited[root] = 1
	queue = [root,-1]
	queue = deque(queue)
	value = 1
	while len(queue)!=0:
		element = queue.popleft()
		if element != -1:
			ans[element] = value
			for i in (graph[element]):
				if visited[i]==0:
					queue.append(i)
			queue.append(-1)
		else:
			value+=1

 
n=int(input())
l=list(map(int,input().split()))
graph=[[] for i in range(n)]
ans=[0]*n
for i in range(n):
	if i+l[i]<=n-1:
		if l[i+l[i]]%2!=l[i]%2:
			ans[i]=1
		else:
			graph[i+l[i]].append(i)
	elif i-l[i]>=0:
		if l[i-l[i]]%2!=l[i]%2:
			ans[i]=1
		else:
			graph[i-l[i]].append(i)
root=-1
for i in range(n):
	if len(graph[i])!=0 and ans[i]!=0:
		root = i
		break

if root != -1:
	bfs(root,graph)
for i in range(n):
	if ans[i]==0:
		ans[i]=-1

print (*ans)