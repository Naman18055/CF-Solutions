import sys
input = sys.stdin.readline
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

	def bfs(self, root): # NORMAL BFS
		queue = [root]
		queue = deque(queue)
		vis = [0]*self.n
		while len(queue)!=0:
			element = queue.popleft()
			vis[element] = 1
			for i in self.graph[element]:
				if vis[i]==0:
					queue.append(i)
					self.parent[i] = element
					vis[i] = 1

	def dfs(self, root): # Iterative DFS
		ans = [0]*n
		stack=[root]
		vis=[0]*self.n
		stack2=[]
		while len(stack)!=0: # INITIAL TRAVERSAL
			element = stack.pop()
			if vis[element]:
				continue
			vis[element] = 1
			stack2.append(element)
			for i in self.graph[element]:
				if vis[i]==0:
					self.parent[i] = element
					stack.append(i)

		node = -1
		while len(stack2)!=0: # BACKTRACING. Modify the loop according to the question
			element = stack2.pop()
			m = 0
			for i in self.graph[element]:
				if i!=self.parent[element]:
					m += ans[i]
			ans[element] = m + 1
			if ans[element]==self.n//2:
				node = element
				break
		return node, self.parent

	def shortestpath(self, source, dest): # Calculate Shortest Path between two nodes
		self.bfs(source)
		path = [dest]
		while self.parent[path[-1]]!=-1:
			path.append(parent[path[-1]])
		return path[::-1]

	def detect_cycle(self):
		indeg = [0]*self.n
		for i in range(self.n):
			for j in self.graph[i]:
				indeg[j] += 1
		q = deque()
		vis = 0
		for i in range(self.n):
			if indeg[i]==0:
				q.append(i)
		while len(q)!=0:
			e = q.popleft()
			vis += 1
			for i in self.graph[e]:
				indeg[i] -= 1
				if indeg[i]==0:
					q.append(i)
		if vis!=self.n:
			return True
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

	def eulertour(self, root):
		stack=[root]
		t = []
		while len(stack)!=0:
			element = stack[-1]
			if vis[element]:
				t.append(stack.pop())
				continue
			t.append(element)
			vis[element] = 1
			for i in self.graph[element]:
				if not vis[i]:
					stack.append(i)
		return t

for nt in range(int(input())):
	n = int(input())
	g = Graph(n, False)
	for i in range(n-1):
		a,b = map(int,input().split())
		edge = [a,b]
		g.addEdge(a-1,b-1)
	if n%2:
		print (edge[0],edge[1])
		print (edge[0],edge[1])
		continue
	node, parent = g.dfs(0)
	if node == -1:
		print (edge[0],edge[1])
		print (edge[0],edge[1])
	else:
		if g.graph[node][1]==parent[node]:
			print (node+1, g.graph[node][0]+1)
			print (parent[node]+1, g.graph[node][0]+1)
		else:
			print (node+1, g.graph[node][1]+1)
			print (parent[node]+1, g.graph[node][1]+1)



