def dfs(root):
	

n=int(input())
parent=[-1]*n
values=[-1]*n
for i in range(n):
	x,y=map(int,input().split())
	if x==0:
		values[i]=(y)
		continue
	parent[i]=x-1
	values[i]=y
print (parent)
print (values)
