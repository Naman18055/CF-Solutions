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
		dist = [0]*n
		while len(queue)!=0:
			element = queue.popleft()
			vis[element] = 1
			for i in self.graph[element]:
				if vis[i]==0:
					queue.append(i)
					self.parent[i] = element
					dist[i] = dist[element]+1
					vis[i] = 1
		return dist.index(max(dist))


	def dfs(self, root, ans): # Iterative DFS
		stack=[root]
		vis=[0]*self.n
		stack2=[]
		dist = [0]*n
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
			m = {}
			maxx = 0
			for i in self.graph[element]:
				if i!=self.parent[element]:
					m[i] = dist[i]
					maxx = max(maxx,dist[i])
			ans[element] = m
			if ans[element]:
				dist[element] = maxx+1
			else:
				dist[element] = 0
		return ans,dist

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

	def calc(self,root):
		add = 0
		done = {root:0}
		while True:
			v = ans[root].values()
			v.append(add)
			v.sort()
			for i in self.graph[root]:
				if ans[root][i]==v[-1]:
					root = i
					add = v[-2]

	def bfs2(self,root,arr):
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
					arr[i] = arr[element]+1
					vis[i] = 1
		return arr







for nt in range(int(input())):
	n,a,b,da,db = map(int,input().split())
	g = Graph(n,False)
	for i in range(n-1):
		u,v = map(int,input().split())
		g.addEdge(u-1,v-1)
	if da>=((db-1)//2+1):
		print ("Alice")
		continue
	d = [0]*n
	d = g.bfs2(a-1,d)
	if d[b-1]<=da:
		print ("Alice")
		continue
		
	e1 = g.bfs(a-1)
	e2 = g.bfs(e1)
	d1 = [0]*n
	d2 = [0]*n
	d1 = g.bfs2(e1,d1)
	d2 = g.bfs2(e2,d2)
	f = []
	for i in range(n):
		f.append(max(d1[i],d2[i]))

	# print (e1,e2)
	# print (d1)
	# print (d2)

	if min(f)<=da:
		print ("Alice")
	else:
		print ("Bob")







