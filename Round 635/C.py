from collections import deque
import sys
# sys.setrecursionlimit(500000)
input = sys.stdin.readline

def bfs(root):
	vis=[0]*n
	queue=[root,-1]
	h=1
	queue=deque(queue)
	while len(queue)!=1:
		element = queue.popleft()
		if element==-1:
			h+=1
			queue.append(-1)
			continue
		vis[element]=1
		flag=0
		for i in tree[element]:
			# print (element,i)
			if vis[i]==0:
				flag=1
				depth[i]=(h,i)
				queue.append(i)
				vis[i]=1
		# if flag==0:
		# 	leaf.append(element)

def dfs(root):
	visited=[0]*n
	stack=[root]
	anss=[]
	while len(stack)!=0:
		element=stack.pop()
		anss.append(element)
		flag=0
		visited[element]=1
		for i in tree[element]:
			if visited[i]==0:
				visited[i]=1
				flag=1
				stack.append(i)
		if flag==0:
			height[element].append(0)
			s[element]=0
	# print (anss)
	# visited=[0]*n
	while len(anss)!=0:
		element = anss.pop()
		# visited[element]=1
		ans=0
		for i in tree[element]:
			if len(height[i])>0:
				ans+=s[i]+1
				height[element].append(s[i]+1)
		s[element]=ans


	# for i in tree[root]:
	# 	# print (i)
	# 	if visited[i]==0:
	# 		visited[i]=1
	# 		x=dfs(i)+1
	# 		ans+=x
	# 		height[root].append(x)
	# 		# print (root,height,x)
	# # height[root].append(0)
	# # return sum(height[root])
	# return ans


n,k=map(int,input().split())
tree=[[] for i in range(n)]
for i in range(n-1):
	a,b=map(int,input().split())
	tree[a-1].append(b-1)
	tree[b-1].append(a-1)
depth=[0]*n
depth[0]=(0,0)
height=[[] for i in range(n)]
s=[0]*n
bfs(0)
dfs(0)

depth.sort(reverse=True)
# print (depth)
# print (height)

ans=[]
for i in range(n):
	if len(height[depth[i][1]])==0:
		ans.append(depth[i][0])
	else:
		ans.append(depth[i][0]-sum(height[depth[i][1]]))
	# print (ans)
# print (leaf)
# ld=[]
# for i in leaf:
# 	ld.append(depth[i])
# ld.sort(reverse=True)
# ans=0
# ans=sum(ld[0:min(k,len(ld))])
# left = k-len(ld)
# if left==0:
# 	print (ans)
# 	exit()
# i=0
# n=len(ld)
# while left!=0:
# 	print (ans,left,i)
# 	if ld[i%n]-(i//n+2)>=0:
# 		ans+=(ld[i%n]-(i//n+2))
# 		left-=1
# 	i+=1
ans.sort(reverse=True)
print (sum(ans[0:k]))

