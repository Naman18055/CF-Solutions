n,m=map(int,input().split())
# graph=[[] for i in range(n)]
# weight=[[] for i in range(n)]
net=[]
for i in range(n):
	net.append((i+1,0))
for i in range(m):
	a,b,c=map(int,input().split())
	net[a-1][1]+=c
	net[b-1][1]-=c
	# graph[a].append(b)
	# weight[a].append(c)
net.sort(key = lambda temp:temp[1])

