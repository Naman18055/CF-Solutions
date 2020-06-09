import sys
input = sys.stdin.buffer.readline
from collections import deque

class Graph(object):
	"""docstring for Graph"""
	def __init__(self,n,d): # Number of nodes and d is True if directed
		self.n = n
		self.graph = [[] for i in range(n)]
		self.parent = [-1 for i in range(n)]
		self.directed = d
		
	def addEdge(self,x,y):
		self.graph[x].append(y)
		if not self.directed:
			self.graph[y].append(x)

	def calc(self, c1, c2):
		if c1==1 and c2==2:
			return 3
		elif c1==1:
			return 2
		elif c1==2 and c2==3:
			return 1
		elif c1==2:
			return 3
		elif c1==3 and c2==1:
			return 2
		else:
			return 1

	def bfs(self, root, c1, c2): # NORMAL BFS
		self.parent = [-1 for i in range(self.n)]
		queue = [root]
		queue = deque(queue)
		vis = [0]*self.n
		color[root] = c1+1
		while len(queue)!=0:
			element = queue.popleft()
			vis[element] = 1
			for i in self.graph[element]:
				if vis[i]==0:
					queue.append(i)
					self.parent[i] = element
					if self.parent[element]==-1:
						color[i] = c2+1
					else:
						color[i] = self.calc(color[element],color[self.parent[element]])
		# print (color)

def value(arr):
	ans=0
	for i in range(n):
		if arr[i]==1:
			ans+=a1[i]
		elif arr[i]==2:
			ans+=a2[i]
		else:
			ans+=a3[i]
	return ans

n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a3=list(map(int,input().split()))
g=Graph(n,False)
for i in range(n-1):
	a,b=map(int,input().split())
	g.addEdge(a-1,b-1)
dp=[0]*n
root=-1
for i in range(n):
	if len(g.graph[i])==1:
		root=i
	elif len(g.graph[i])>2:
		root=-1
		break
if root==-1:
	print (-1)
	exit()
ans,fans=10**18,[]

color=[0]*n
g.bfs(root,0,1)
if value(color)<ans:
	ans=value(color)
	fans=color[::]

color=[0]*n
g.bfs(root,0,2)
value(color)
if value(color)<ans:
	ans=value(color)
	fans=color[::]

color=[0]*n
g.bfs(root,1,0)
value(color)
if value(color)<ans:
	ans=value(color)
	fans=color[::]

color=[0]*n
g.bfs(root,1,2)
value(color)
if value(color)<ans:
	ans=value(color)
	fans=color[::]

color=[0]*n
g.bfs(root,2,1)
value(color)
if value(color)<ans:
	ans=value(color)
	fans=color[::]

color=[0]*n
g.bfs(root,2,0)
value(color)
if value(color)<ans:
	ans=value(color)
	fans=color[::]

print (ans)
print (*fans)




