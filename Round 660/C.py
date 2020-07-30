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
			count[element][0] = (passed[element] + h[element])//2
			count[element][1] = passed[element] - count[element][0]


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
			ans[element] = m + p[element]
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

	def check(self):
		q = [0]
		q = deque(q)
		vis = [0]*n
		while q:
			e = q.popleft()
			vis[e] = 1
			c = 0
			for i in self.graph[e]:
				if not vis[i]:
					q.append(i)
					c += count[i][1]
			if c<(count[e][1]-p[e]):
				return False
			if (passed[e] + h[e])%2 or (count[e][0]<0) or count[e][1]<0:
				return False
		return True


for nt in range(int(input())):
	n,m = map(int,input().split())
	p = list(map(int,input().split()))
	h = list(map(int,input().split()))
	g = Graph(n,False)
	for i in range(n-1):
		x,y = map(int,input().split())
		g.addEdge(x-1,y-1)
	passed = [0]*n
	count = [[0,0] for i in range(n)]
	passed = g.dfs(0,passed)
	g.bfs(0)
	# print (passed)
	# print (count)
	if g.check():
		print ("YES")
	else:
		print ("NO")






