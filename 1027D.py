# import sys
# input = sys.stdin.buffer.readline
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

	def ifcycle(self, root, vis):
		self.bfs(root)
		queue = [root]
		queue = deque(queue)
		done = {root:1}
		prev = root
		while len(queue)!=0:
			element = queue.popleft()
			prev = element
			vis[element] = 1
			for i in self.graph[element]:
				if i in done:
					cycle = [element]
					while cycle[-1]!=i:
						cycle.append(self.parent[cycle[-1]])
					return (True,cycle)

				if vis[i]==1:
					return (False,-1)

				if vis[i]==0:
					done[i]=1
					queue.append(i)
					vis[i] = 1
		return (False,prev)

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



n = int(input())
g = Graph(n,True)
cost = list(map(int,raw_input().split()))
l = list(map(int,raw_input().split()))
vis = [0]*n
ans = 0
for i in range(n):
	if vis[i]==0:
		curr=i
		temp = cost[curr]
		flag = 0
		done = {curr:1}
		while True:
			if vis[curr]==1:
				if curr not in done:
					flag = 2
					break
				flag = 1
				break
			done[curr]=1
			vis[curr]=1
			if curr!=l[curr]-1:
				temp = cost[l[curr]-1]
			else:
				break
			curr = l[curr]-1
		if flag==2:
			continue
		if not flag:
			ans+=temp
		else:
			nxt = l[curr]-1
			temp = cost[nxt]
			while nxt!=curr:
				nxt = l[nxt]-1
				temp = min(cost[nxt],temp)
			ans+=temp
		# print (ans,temp,flag,i)

print (ans)