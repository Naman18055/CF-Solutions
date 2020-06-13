import sys
input = sys.stdin.readline
from queue import PriorityQueue
n,m = map(int,input().split())
graph = [[] for i in range(n)]
e = {}
for i in range(m):
	x,y = map(int,input().split())
	if x!=y and (x,y) not in e:
		e[(x,y)] = 1
		e[(y,x)] = 1
		graph[x-1].append(y-1)
		graph[y-1].append(x-1)
q = PriorityQueue()
vis = [0]*n
q.put(0)
while not q.empty():
	e = q.get()
	if vis[e]:
		continue
	vis[e] = 1
	print (e+1,end=" ")
	for i in graph[e]:
		if not vis[i]:
			q.put(i)
print ()