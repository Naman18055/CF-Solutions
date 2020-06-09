from collections import deque
import sys
input = sys.stdin.readline

def bfs(root):
	queue = [root]
	queue = deque(queue)
	vis = [0]*n
	while len(queue)!=0:
		element = queue.popleft()
		vis[element] = 1
		for i in graph[element]:
			if vis[i]==0:
				queue.append(i)
				vis[i]=1
				parent[i]=element

def dfs(root):
	stack=[root]
	vis=[0]*n
	vis[root]=1
	stack2=[]
	while len(stack)!=0:
		element = stack.pop()
		vis[element] = 1
		stack2.append(element)
		for i in graph[element]:
			if vis[i]==0:
				vis[i]=1
				stack.append(i)
	while len(stack2)!=0:
		element = stack2.pop()
		m = 0
		for i in graph[element]:
			if i!=parent[element]:
				m += max(0,values[i])
		if l[element]==0:
			values[element]=m-1
		else:
			values[element]=m+1

def reroot(root):
	stack=[root]
	vis=[0]*n
	while len(stack)!=0:
		element = stack[-1]
		if vis[element] == 1:
			stack.pop()
			if parent[element]==-1:
				continue
			values[element] -= max(0,values[parent[element]])
			values[parent[element]] += max(0,values[element])
			continue
		vis[element] = 1
		for i in graph[element]:
			if vis[i]==0:
				stack.append(i)
		if parent[element]==-1:
			continue
		values[parent[element]] -= max(0,values[element])
		values[element] += max(0,values[parent[element]])
		ans[element] = values[element]
		# print (values,element,stack)


n=int(input())
l=list(map(int,input().split()))
graph=[[] for i in range(n)]
for i in range(n-1):
	a,b=map(int,input().split())
	graph[a-1].append(b-1)
	graph[b-1].append(a-1)
values=[-n]*n
parent=[-1]*n
bfs(0)
dfs(0)
ans=[-1]*n
ans[0]=values[0]
# print (values)
reroot(0)
print (*ans)