import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
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
		dist = [0]*self.n
		while len(queue)!=0:
			element = queue.popleft()
			vis[element] = 1
			for i in self.graph[element]:
				if vis[i]==0:
					queue.append(i)
					self.parent[i] = element
					dist[i] = dist[element] + 1
					vis[i] = 1
		return dist

	def dfs(self, root, minn): # Iterative DFS
		ans = [i for i in minn]
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
		# print (stack2)
		while len(stack2)!=0: # BACKTRACING. Modify the loop according to the question
			element = stack2.pop()
			m = minn[element]
			for i in self.graph[element]:
				if i!=self.parent[element]:
					m = min(m, ans[i])
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

for nt in range(int(input())):
	input()
	n, m = map(int, input().split())
	adj = [[] for xy in range(n)]
	for xy in range(m):
		u, v = map(lambda x: int(x) - 1, input().split())
		adj[u].append(v)
	dis = [-1] * n
	dis[0] = 0
	que = [0]
	for i in range(n):
		u = que[i]
		for v in adj[u]:
			if dis[v] == -1:
				dis[v] = dis[u] + 1
				que.append(v)
	ans = [0] * n
	for u in sorted([i for i in range(n)], key=lambda x: dis[x], reverse=True):
		ans[u] = dis[u]
		for v in adj[u]:
			if dis[u] >= dis[v]:
				ans[u] = min(ans[u], dis[v])
			else:
				ans[u] = min(ans[u], ans[v])
	print(*ans)
























