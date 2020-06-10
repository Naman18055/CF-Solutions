x,y,ax,ay,bx,by=map(int,input().split())
sx,sy,t=map(int,input().split())
data=[(x,y)]
while data[-1][0]<=10**16 and data[-1][1]<=10**16:
	new=(data[-1][0]*ax+bx,data[-1][1]*ay+by)
	data.append(new)
ans=0
for ind in range(len(data)):
	prev=(sx,sy)
	count = 0
	time = 0
	for i in range(ind,-1,-1):
		time+=(abs(data[i][0]-prev[0])+abs(data[i][1]-prev[1]))
		if time<=t:
			count+=1
			prev=data[i]
		else:
			break
	for i in range(ind+1,len(data)):
		time+=((abs(data[i][0]-prev[0])+abs(data[i][1]-prev[1])))
		if time<=t:
			count+=1
			prev=data[i]
		else:
			break
			#print (time)
	ans = max(ans,count)
print (ans)
