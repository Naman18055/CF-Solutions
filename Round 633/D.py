from collections import deque
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(300000)

def dfs(root):
	stack=[root]
	while len(stack)!=0:
		element = stack.pop()
		for i in tree[element]:
			if num[i]==-1:
				stack.append(i)
				num[i]=1-num[element]


def bfs(root):
	queue=[root]
	queue=deque(queue)
	vis=[-1]*n
	while len(queue)!=0:
		element = queue.popleft()
		vis[element]=1
		for i in tree[element]:
			if vis[i]==-1:
				queue.append(i)
				child[element].append(i)
				vis[i]=1
			if len(tree[element])==1:
				leaf.append(element)


n=int(input())
tree=[[] for i in range(n)]
child=[[] for i in range(n)]
for i in range(n-1):
	a,b=list(map(int,input().split()))
	tree[a-1].append(b-1)
	tree[b-1].append(a-1)
leaf=[]
bfs(0)
num=[-1]*n
num[leaf[0]]=0
dfs(leaf[0])
minimum=1
for i in leaf:
	if num[i]!=num[leaf[0]]:
		minimum=3
		break
maximum=n-1
leaf = set(leaf)
for i in range(n):
	flag=0
	for j in tree[i]:
		if j in leaf:
			maximum-=1
			flag=1
	if flag:
		maximum+=1
print (minimum,maximum)
