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

	def dfs(self, root, ans): # Iterative DFS
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

		while len(stack2)!=0: # BACKTRACING. Modify the loop according to the question
			element = stack2.pop()
			m = 0
			for i in self.graph[element]:
				if i!=self.parent[element]:
					m += ans[i]
			ans[element] = m
		return ans

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
		ans = []
		for i in range(self.n):
			if indeg[i]==0:
				q.append(i)
		while len(q)!=0:
			e = q.popleft()
			ans.append(e)
			vis += 1
			for i in self.graph[e]:
				indeg[i] -= 1
				if indeg[i]==0:
					q.append(i)
		if vis!=self.n:
			return True,[]
		return False,ans

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

	# def find(self, parent, i): 
	# 	if parent[i] == i: 
	# 		return i 
	# 	return self.find(parent, parent[i]) 
  

	# def union(self, parent, rank, x, y): 
	# 	xroot = self.find(parent, x) 
	# 	yroot = self.find(parent, y) 
	# 	if rank[xroot] < rank[yroot]: 
	# 		parent[xroot] = yroot 
	# 	elif rank[xroot] > rank[yroot]: 
	# 		parent[yroot] = xroot 
	# 	else : 
	# 		parent[yroot] = xroot 
	# 		rank[xroot] += 1

	# def solve(self,x,y):
	# 	if len(self.graph[x])>0 and indeg[x]==0:
	# 		self.addEdge(x,y)
	# 		indeg[y] += 1
	# 	elif len(self.graph[x])==0 and indeg[x]>0:
	# 		self.addEdge(y,x)
	# 		indeg[x] += 1
	# 	elif len(self.graph[y])>0 and indeg[y]==0:
	# 		self.addEdge(y,x)
	# 		indeg[x] += 1
	# 	elif len(self.graph[y])==0 and indeg[y]>0:
	# 		self.addEdge(x,y)
	# 		indeg[y] += 1
	# 	else:
	# 		self.addEdge(x,y)
	# 		# indeg[y] += 1
	# 		if g.detect_cycle():
	# 			self.graph[x].pop()
	# 			g.addEdge(y,x)
	# 			indeg[x] += 1
	# 		else:
	# 			indeg[y] += 1





for nt in range(int(input())):
	n,m = map(int,input().split())
	g = Graph(n,True)
	edges = []
	for i in range(m):
		t,x,y = map(int,input().split())
		if t==1:
			g.addEdge(x-1,y-1)
		else:
			edges.append((x-1,y-1))
	x = g.detect_cycle()
	# print (x)
	if x[0]:
		print ("NO")
		continue

	top = x[1]
	loc = {}
	for i in range(n):
		loc[top[i]] = i

	for i in edges:
		if loc[i[0]]<loc[i[1]]:
			g.addEdge(i[0],i[1])
		else:
			g.addEdge(i[1],i[0])

	if g.detect_cycle()[0]:
		print ("NO")
		continue
	print ("YES")
	for i in range(n):
		for j in g.graph[i]:
			print (i+1,j+1)