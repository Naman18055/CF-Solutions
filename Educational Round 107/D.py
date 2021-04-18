import sys
input = sys.stdin.readline
from collections import deque

class Graph(object):
	"""docstring for Graph"""
	def __init__(self,n,d): # Number of nodes and d is True if directed
		self.n = n
		self.graph = [[] for i in range(n)]
		self.parent = [-1 for i in range(n)]
		self.child = {}
		self.directed = d
		self.total_edges = 0
		
	def addEdge(self,x,y):
		self.total_edges += 1
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

	# TRY EXPERIMENTING BY REPLACING STACK2 WITH EULER TOUR AND TAKING THE SECOND OCCURRENCE FROM BACK
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

	def eulertour(self, root): # Order in which vertices are visited in DFS
		stack=[root]
		t = []
		vis = [0]*self.n
		while len(stack)!=0:
			element = stack[-1]
			if vis[element]:
				t.append(stack.pop())
				continue
			t.append(element)
			vis[element] = 1
			for i in self.graph[element]:
				if not vis[i]:
					self.parent[i] = element
					stack.append(i)
		c = {}
		ans = []
		for i in t:
			if i not in c:
				ans.append(i)
				c[i] = 1
			elif c[i]!=2:
				ans.append(i)
				c[i] += 1
		return ans

	def articulation_points(self): # UNTESTED
		at = [0]*self.n
		order = self.eulertour(0)
		done = {}
		disc = [0]*self.n
		low = [0]*self.n
		time = 0 
		for i in order:
			if i not in done:
				done[i] = 1
				if self.parent[i] != -1:
					disc[i] = time+1
					time += 1
					low[i] = disc[i]
		after = {}
		for i in range(self.n):
			if self.parent[i] not in after:
				after[self.parent[i]] = [i]
			else:
				after[self.parent[i]].append(i)
		dfs_order = []
		done = {}
		for i in order[::-1]:
			if i not in done:
				done[i] = 1
			else:
				dfs_order.append(i)
		for i in dfs_order:
			for j in self.graph[i]:
				if i in after and j in after[i]:
					low[i] = min(low[i], low[j])
					if i==0 and len(after[i])>1:
						at[i] = 1
					if i!=0 and low[j]>=disc[i]:
						at[i] = 1
				elif j!=self.parent[i]:
					low[i] = min(low[i], disc[j])
		return at

	def eulerian_path(self): # Assumes conditions reqd are satisfied
		curr_path = [0]
		cycle = []
		while curr_path:
			node = curr_path[-1]
			if self.graph[node]:
				nxt = self.graph[node].pop()
				curr_path.append(nxt)
			else:
				cycle.append(curr_path.pop())
		return cycle[::-1]



n, k = map(int,input().split())
g = Graph(k, True)
for i in range(k):
	for j in range(k):
		if i==j:
			continue
		g.addEdge(i, j)
ans = g.eulerian_path()
f = chr(ans[0]+97)
f += f[-1]
done = {0:1}
for i in range(1, len(ans)):
	f += chr(ans[i]+97)
	if ans[i] not in done:
		done[ans[i]] = 1
		f += f[-1]
ans = f
while len(ans)<n:
	ans += f[-k**2:]
print (ans[0:n])
