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

for nt in range(int(input())):
	n = int(input())
	w = list(map(int,input().split()))
	g = Graph(n, False)
	final = [sum(w)]
	for i in range(n-1):
		x, y = map(int,input().split())
		g.addEdge(x-1, y-1)
	if n==2:
		print (sum(w))
		continue

	count = {}
	for i in range(n):
		if len(g.graph[i])>1:
			if w[i] in count:
				count[w[i]] += (len(g.graph[i])-1)
			else:
				count[w[i]] = (len(g.graph[i])-1)
	arr = []
	for i in count:
		arr.append([i, count[i]])
	arr.sort()
	i = len(arr)-1
	# print (count)
	# print (arr)
	while i>=0:
		if arr[i][1]:
			final.append(final[-1]+arr[i][0])
			arr[i][1] -= 1
		else:
			i -= 1
	print (*final)






















