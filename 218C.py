def dfs(node):
	vis[node]=1
	for i in range(n):
		if (X[i]==X[node] or Y[i]==Y[node]) and vis[i]==0:
			dfs(i)

r=[-1 for i in range(2005)] 
n=int(input()) 
X,Y=[],[] 
vis=[0]*101
for i in range(n):
	x,y=map(int,input().split())
	X.append(x)
	Y.append(y)
ans=0
for i in range(n):
	if (vis[i]==0):
		dfs(i)
		ans+=1
print(ans-1)