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

	def bfs(self, root, depth): # NORMAL BFS
		queue = [root]
		queue = deque(queue)
		vis = [0]*self.n
		while len(queue)!=0:
			element = queue.popleft()
			vis[element] = 1
			for i in self.graph[element]:
				if vis[i]==0:
					if depth[i]!=depth[element]+1:
						return False
					queue.append(i)
					self.parent[i] = element
		return True

	def dfs(self, root, ans): # Iterative DFS
		queue = [root]
		queue = deque(queue)
		vis = [0]*self.n
		while len(queue)!=0:
			element = queue.popleft()
			vis[element] = 1
			for i in self.graph[element]:
				if vis[i]==0:
					ans[i]=ans[element]+1
					queue.append(i)
					self.parent[i] = element
		return ans

	def shortestpath(self, source, dest): # Calculate Shortest Path between two nodes
		self.bfs(source)
		path = [dest]
		while self.parent[path[-1]]!=-1:
			path.append(parent[path[-1]])
		return path[::-1]

	def ifcycle(self):
		self.bfs(0)
		queue = [0]
		vis = [0]*n
		queue = deque(queue)
		while len(queue)!=0:
			element = queue.popleft()
			vis[element] = 1
			for i in graph[element]:
				if vis[i]==1 and i!=parent[element]:
					return True
				if vis[i]==0:
					queue.append(i)
					vis[i] = 1
		return False

	def reroot(self, root, ans):
		stack = [root]
		vis = [0]*n
		while len(stack)!=0:
			e = stack[-1]
			if vis[e]:
				stack.pop()
				# Reverse_The_Change()
				continue
			vis[e] = 1
			for i in graph[e]:
				if not vis[e]:
					stack.append(i)
			if self.parent[e]==-1:
				continue
			# Change_The_Answers()

	def lastcheck(self, root, depth):
		queue = [root]
		queue = deque(queue)
		vis = [0]*self.n
		while len(queue)!=0:
			element = queue.popleft()
			vis[element] = 1
			if depth[element] != k+1 and len(self.graph[element])<=3 and element!=root:
				return False
			for i in self.graph[element]:
				if vis[i]==0:
					queue.append(i)
					self.parent[i] = element
		return True

	def check(self):
		root = -1
		for i in range(self.n):
			if len(self.graph[i])==1:
				root = i
				break
		if root == -1:
			return False
		depth = [1]*self.n
		depth = self.dfs(root, depth)
		# print (depth)
		# print (self.parent)
		end = -1
		for i in range(self.n):
			if depth[i]==(2*k+1):
				end = i
				for j in range(k):
					end = self.parent[end]
					if end == -1:
						return False
				break
		# print (end)
		if end == -1:
			return False
		root = end
		depth = [1]*self.n
		depth = self.dfs(root, depth)
		# print (depth)
		for i in range(self.n):
			if len(self.graph[i])==1 and depth[i]!=k+1:
				return False
			if len(self.graph[i])==2:
				return False
		if self.lastcheck(root, depth):
			return True
		return False

n,k=map(int,input().split())
g=Graph(n,False)
for i in range(n-1):
	u,v=map(int,input().split())
	g.addEdge(u-1,v-1)

if g.check():
	print ("Yes")
else:
	print ("No")