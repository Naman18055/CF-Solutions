import sys
import heapq
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
		dist = {root:0}
		ans = 0
		while len(queue)!=0:
			element = queue.popleft()
			vis[element] = 1
			flag = 0
			for i in self.graph[element]:
				if vis[i]==0:
					queue.append(i)
					self.parent[i] = element
					vis[i] = 1
					dist[i] = dist[element] + weight[element,i]
					flag = 1
			if not flag:
				ans += dist[element]
		return dist,ans

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
			flag = 0
			for i in self.graph[element]:
				if i!=self.parent[element]:
					m += ans[i]
					flag = 1
			if not flag:
				ans[element] = 1
			else:
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

answers = []
for nt in range(int(input())):
	n,s = map(int,input().split())
	g = Graph(n,False)
	weight = {}
	h = []
	count = [0]*n
	for i in range(n-1):
		x,y,w = map(int,input().split())
		g.addEdge(x-1,y-1)
		weight[x-1,y-1] = w
		weight[y-1,x-1] = w

	dist,d = g.bfs(0)
	count = g.dfs(0,count)
	check = 0
	for i in range(1,n):
		temp = weight[(i,g.parent[i])]*count[i]
		h.append((-(temp-((weight[(i,g.parent[i])]//2)*count[i])),(weight[(i,g.parent[i])]*count[i]),count[i]))
		check += weight[(i,g.parent[i])]*count[i]

	heapq.heapify(h)
	if check!=d:
		print (1/0)
		exit()

	# print (dist)
	# print (count)
	# print (d)
	# print (h)
	d = check
	ans = 0
	while d>s:
		sub = heapq.heappop(h)
		d += sub[0]
		x = sub[1]//sub[2]
		x = x//2
		temp = x*sub[2]
		heapq.heappush(h,(-(temp-((x//2)*sub[2])),temp,sub[2]))

		ans += 1
		# print (d,h)

	answers.append(ans)

for i in answers:
	print (i)




