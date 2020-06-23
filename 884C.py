import sys
sys.setrecursionlimit(10000)

def dfs(root,t):
	time[root]=t
	vis[root]=1
	stack=[root]
	while (len(stack)!=0):
		element = stack.pop()
		time[element] = t
		vis[element] = 1
		for i in graph[element]:
			if vis[i]==0:
				stack.append(i)
				t+=1
			else:
				c.append(t-time[i]+1)
	# for i in graph[root]:
	# 	if vis[i]==0:
	# 		dfs(i,t+1)
	# 	else:
	# 		c.append(t-time[i]+1)


n=int(input())
l=list(map(int,input().split()))
graph=[[] for i in range(n)]
for i in range(n):
	graph[i].append(l[i]-1)
# print (graph)
vis=[0]*n
c=[]
time=[0]*n
for i in range(n):
	if vis[i]==0:
		dfs(i,1)
# print (time)
# print (c)
c.sort()
ans=0
for i in c:
	ans+=i**2
if len(c)>=2:
	print (ans+c[-1]*c[-2]*2)
else:
	print (ans)