import sys
input = sys.stdin.readline
from collections import deque

class Graph(object):
	"""docstring for Graph"""
	def __init__(self,n,d): # Number of nodes and d is True if directed
		self.n = n
		self.graph = {}
		self.parent = [-1 for i in range(n)]
		self.directed = d
		
	def addEdge(self,x,y):
		if x not in self.graph:
			self.graph[x] = set()
		self.graph[x].add(y)

		if not self.directed:
			if y not in self.graph:
				self.graph[y] = set()
			self.graph[y].add(x)

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

	def calc(self):
		q = deque()
		for i in range(self.n):
			if len(self.graph[i])==1:
				q.append(i)
		cnt = [1]*n
		while q:
			e = q.popleft()
			for i in self.graph[e]:
				p = i
			cnt[p] += cnt[e]
			self.graph[e].remove(p)
			self.graph[p].remove(e)
			if len(self.graph[p])==1:
				q.append(p)
		return self.graph, cnt


for nt in range(int(input())):
	n = int(input())
	g = Graph(n, False)
	for i in range(n):
		a, b = map(int,input().split())
		g.addEdge(a-1, b-1)

	graph, arr = g.calc()
	v = []
	for i in graph:
		if not graph[i]:
			continue
		v.append(i)

	ans = 0
	for i in v:
		c = arr[i]
		ans += (c*(c-1))//2 + c*(n-c)
	print (ans)



