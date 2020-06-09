from collections import deque

def bfs(root):
	vis=[0]*n
	queue = [root]
	queue = deque(queue)
	while len(queue)!=0:
		e = queue.popleft()
		vis[e]=1
		for i in graph[e]:
			if vis[i]==0:
				queue.append(i)
				vis[i]=1

for nt in range(int(input())):
	n,x=map(int,input().split())
	x-=1
	graph = [[] for i in range(n)]
	for i in range(n-1):
		a,b=map(int,input().split())
		graph[a-1].append(b-1)
		graph[b-1].append(a-1)
	bfs(x)
	count = len(graph[x])
	if count<=1:
		print ("Ayush")
		continue
	left = n-(count+1)
	if left%2:
		turn = 1
	else:
		turn = 0
	if count%2:
		if turn==1:
			print ("Ashish")
		else:
			print ("Ayush")
	else:
		if turn==0:
			print ("Ashish")
		else:
			print ("Ayush")
