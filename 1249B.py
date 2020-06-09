import sys
from collections import deque
input = sys.stdin.readline


def bfs(root):
	q = [root]
	q = deque(q)
	count = 1
	while len(q)!=0:
		e = q.popleft()
		done[e] = 1
		for i in graph[e]:
			if done[i]==0:
				q.append(i)
				parent[i] = e
				count += 1
			else:
				s = e
				ans[s] = count
				while parent[s]!=-1:
					s = parent[s]
					ans[s] = count

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	graph = [[] for i in range(n)]
	for i in range(n):
		graph[i].append(a[i]-1)
	done = [0]*n
	parent = [-1]*n
	ans = [0]*n
	for i in range(n):
		if done[i]==0:
			bfs(i)
			done[i]=1
	print (*ans)

