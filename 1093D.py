mod = 998244353
# import sys
# input = sys.stdin.buffer.readline
from collections import deque
# sys.setrecursionlimit(100000)

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

	def bfs(self,root): # NORMAL BFS
		self.parent = [-1 for i in range(n)]
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

	def shortestpath(source, dest): # Calculate Shortest Path between two nodes
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

	def dfss(self, root, vis):

		# vis=[0]*self.n
		color=[-1]*self.n
		color[root]=0
		# self.pdfs(root,vis,color)
		# return
		stack=[root]
		while len(stack)!=0:
			e=stack.pop()
			if vis[e]:
				continue

			if color[e]==-1:
				if color[self.parent[e]]:
					color[e]=0
					l1[-1]+=1
				else:
					color[e]=1
					l2[-1]+=1
			vis[e]=1

			for i in self.graph[e]:
				if color[i]==color[e]:
					return False
				if not vis[i]:
					stack.append(i)
					self.parent[i]=e

		return True

def calc(t1,t2):
	ans=0
	ans+=(pow(2,t1,mod))%mod
	ans+=(pow(2,t2,mod))%mod
	return (ans)

test=int(input())
for nt in range(test):
	n,m=map(int,raw_input().split())
	if m==0:
		print (pow(3,n,mod))
		continue
	g=Graph(n,False)
	inputs = []
	for i in range(m):
		x,y=map(int,raw_input().split())
		g.addEdge(x-1,y-1)
		inputs.append((x,y))
	l1,l2=[],[]
	vis=[0]*n
	flag=0
	for i in range(n):
		if not vis[i]:
			l1.append(1)
			l2.append(0)
			ans = g.dfss(i,vis)
			if not ans:
				flag=1
				break

	if flag:
		print (0)
		continue

	ans=1
	for i in range(len(l1)):
		temp=calc(l1[i],l2[i])
		if temp==-1:
			ans=(0)
			break
		ans=(ans*temp)%mod
	print (ans%mod)