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
			ans.append(element)
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
			vis[element] = 1
			stack2.append(element)
			for i in self.graph[element]:
				if vis[i]==0:
					vis[i]=1
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

	def solve(self):
		nodes1={}
		nodes2={}
		for i in range(2*n):
			if len(self.graph[i])>0:
				nodes1[i]=1
				nodes2[self.graph[i][0]]=1
		roots=[]
		for i in nodes1:
			if i not in nodes2:
				roots.append(i)
		# print (roots)
		for root in roots:
			self.bfs(root)
			ans.pop()



value=[-1 for i in range(2800001)]
primes=[]
for i in range(2,2800001):
	if value[i]==-1:
		primes.append(i)
		for j in range(i,2800001,i):
			if value[j]==-1:
				value[j]=i
	else:
		value[i]=i//value[i]
locp={}
for i in range(len(primes)):
	locp[primes[i]]=i+1

n = int(input())
b = list(map(int,input().split()))
b.sort()
new = []
done = [-1]*(2*n)
loc = {}
for i in range(2*n):
	if b[i] in loc:
		loc[b[i]].append(i)
	else:
		loc[b[i]]=[i]
# print (loc)
for i in range(2*n-1,-1,-1):
	if len(new)==n:
		break
	if done[i]==-1:
		if value[b[i]]==b[i]:
			new.append(locp[b[i]])
			# print (b[i],primes[b[i]-1],primes[120])
			done[loc[locp[b[i]]].pop()]=1
		else:
			new.append(b[i])
			done[loc[value[b[i]]].pop()]=1


print (*new)
