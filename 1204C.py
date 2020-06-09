import sys
input = sys.stdin.readline
from collections import deque
class Graph(object):
	"""docstring for Graph"""
	def __init__(self, n):
		self.n = n
		self.graph = [[] for i in range(n)]

	def bfs(self, root):
		queue = [root,-1]
		queue = deque(queue)
		vis = [0]*n
		d = [0]*n
		t = 1
		while len(queue)!=1:
			element = queue.popleft()
			if element==-1:
				queue.append(-1)
				t+=1
				continue
			vis[element] = 1
			for i in self.graph[element]:
				if vis[i]==0:
					queue.append(i)
					d[i] = t
					vis[i] = 1
		# print (d, root)
		return d

n = int(input())
g = Graph(n)
for i in range(n):
	s=input()
	for j in range(n):
		if s[j]=="1":
			g.graph[i].append(j)
k = int(input())
a = list(map(int,input().split()))
dist=[]
for i in range(n):
	dist.append(g.bfs(i))
# print (g.graph)
# for i in dist:
# 	print (*i)

i = 1
root = a[0]-1
d = 1
count = 1
ans = [a[0]]
while i<k:
	# print (root,i,d)
	if dist[root][a[i]-1]!=d:
		count += 1
		root = a[i-1]-1
		ans.append(a[i-1])
		d = 1
	else:
		i += 1
		d += 1
ans.append(a[-1])
count += 1
print (count)
print (*ans)




