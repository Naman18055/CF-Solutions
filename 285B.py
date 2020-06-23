from collections import deque

def bfs(s,t):
	vis = [0]*n
	q = deque()
	q.append(s)
	count = 0
	while len(q)!=0:
		e = q.popleft()
		vis[e] = 1
		if not vis[graph[e]]:
			q.append(graph[e])
			count += 1
			if graph[e]==t:
				return count
		else:
			return -1

n,s,t = map(int,input().split())
a = list(map(int,input().split()))
if s==t:
	print (0)
	exit()
graph = [-1]*n
for i in range(n):
	graph[i] = a[i]-1
s,t = s-1,t-1
print (bfs(s,t))