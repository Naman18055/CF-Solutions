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

	def bfs(self, root): # NORMAL BFS
		self.parent = [-1 for i in range(self.n)]
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

	def check(self, node, blog):
		done = {}
		for i in self.graph[node]:
			if i in b and b[i]<blog:
				done[b[i]] = 1
			if i in b and b[i]==blog:
				return False
		if len(done)==blog-1:
			return True
		return False


n,m = map(int,input().split())
g = Graph(n+1,False)
for i in range(m):
	a,b = map(int,input().split())
	g.addEdge(a,b)
t = list(map(int,input().split()))
l = {}
for i in range(1,n+1):
	if t[i-1] not in l:
		l[t[i-1]] = [i]
	else:
		l[t[i-1]].append(i)
d = {}
b = {}
ans = []
i = 1
flag = 0
# print (g.graph)
# print (l)
while len(d)!=n:
	if i not in l:
		flag = 1
		break
	for j in l[i]:
		if not g.check(j,i):
			flag = 1
			break
		else:
			d[j] = 1
			b[j] = i
			ans.append(j)
	if flag:
		break
	i += 1
if flag:
	print (-1)
	exit()
print (" ".join(map(str,ans)))