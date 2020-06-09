# import sys
# input = sys.stdin.readline
from collections import deque
def path():
	queue = [n*m-1]
	queue = deque(queue)
	vis = [0]*(n*m)
	vis[queue[0]] = 1
	parent = [-1]*(n*m)
	while len(queue)!=0:
		e = queue.popleft()
		vis[e] = 1
		for i in graph[e]:
			done[i]=1
			if vis[i]==0:
				queue.append(i)
				parent[i] = e
				vis[i] = 1

for nt in range(int(input())):
	n,m=map(int,input().split())
	maze=[]
	for i in range(n):
		maze.append(list(input()))
	flag = 0
	ans = "Yes"
	for i in range(n):
		for j in range(m):
			if maze[i][j]=="B":
				# print (i,j,maze)
				if i<n-1 and maze[i+1][j]!="B":
					if maze[i+1][j]=="G":
						flag = 1
						ans = "No"
						break
					maze[i+1][j]="#"
				if j<m-1 and maze[i][j+1]!="B":
					if maze[i][j+1]=="G":
						flag = 1
						ans = "No"
						break
					maze[i][j+1]="#"
				if i>0 and maze[i-1][j]!="B":
					if maze[i-1][j]=="G":
						flag = 1
						ans = "No"
						break
					maze[i-1][j]="#"
				if j>0 and maze[i][j-1]!="B":
					if maze[i][j-1]=="G":
						flag = 1
						ans = "No"
						break
					maze[i][j-1]="#"
				maze[i][j]="#"
		if flag:
			break
	if flag:
		print (ans)
		continue
	graph = [[] for i in range(n*m)]
	for i in range(n):
		for j in range(m):
			if maze[i][j]!="#":
				if i<n-1 and maze[i+1][j]!="#":
					graph[i*m+j].append((i+1)*m+j)
				if i>0 and maze[i-1][j]!="#":
					graph[i*m+j].append((i-1)*m+j)
				if j<m-1 and maze[i][j+1]!="#":
					graph[i*m+j].append(i*m+j+1)
				if j>0 and maze[i][j-1]!="#":
					graph[i*m+j].append(i*m+j-1)
	done = {}
	flag = 0
	path()
	for i in range(n):
		for j in range(m):
			if maze[i][j]=="G":
				if (i*m+j) not in done:
					ans = "No"
					flag = 1
					break
		if flag:
			break
	print (ans)