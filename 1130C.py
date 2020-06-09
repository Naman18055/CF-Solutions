from collections import deque
def bfs(start):
	q=[start]
	q=deque(q)
	allnodes=[start]
	visited[start]=1
	while len(q)!=0:
		element = q.popleft()
		for i in graph[element]:
			if visited[tuple(i)]==0:
				q.append(tuple(i))
				allnodes.append(tuple(i))
				visited[tuple(i)]=1
	return allnodes

n=int(input())
r1,c1=map(int,input().split())
r2,c2=map(int,input().split())
graph={}
m=[]
for i in range(n):
	s=list(input())
	m.append(s)
visited={}
for i in range(n):
	for j in range(n):
		if m[i][j]=="0":
			if i>0:
				if m[i-1][j]=="0":
					if (i,j) in graph:
						graph[(i,j)].append([i-1,j])
					else:
						graph[(i,j)]=[[i-1,j]]
			if j>0:
				if m[i][j-1]=="0":
					if (i,j) in graph:
						graph[(i,j)].append([i,j-1])
					else:
						graph[(i,j)]=[[i,j-1]]
			if i<n-1:
				if m[i+1][j]=="0":
					if (i,j) in graph:
						graph[(i,j)].append([i+1,j])
					else:
						graph[(i,j)]=[[i+1,j]]		
			if j<n-1:
				if m[i][j+1]=="0":
					if (i,j) in graph:
						graph[(i,j)].append([i,j+1])
					else:
						graph[(i,j)]=[[i,j+1]]
			visited[(i,j)]=0
			if (i,j) not in graph:
				graph[(i,j)]=[]
temp1=bfs((r1-1,c1-1))
temp2=bfs((r2-1,c2-1))
m=10000000
for i in temp1:
	for j in temp2:
		if (i[0]-j[0])**2+(i[1]-j[1])**2<m:
			m=(i[0]-j[0])**2+(i[1]-j[1])**2
print (m)


