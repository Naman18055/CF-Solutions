x,y,ax,ay,bx,by=map(int,input().split())
sx,sy,t=map(int,input().split())
data=[(1,1)]
while data[-1][0]<=10**16 and data[-1][1]<=10**16:
	new=(data[-1][0]*ax+bx,data[-1][1]*ay+by)
	data.append(new)
initialtime={}
m=10**18
for i in range(len(data)):
	initialtime[data[i]]=abs(data[i][0]-sx)+abs(data[i][1]-sy)
	if abs(data[i][0]-sx)+abs(data[i][1]-sy)<m:
		m=abs(data[i][0]-sx)+abs(data[i][1]-sy)
		coor=data[i]
		ind=i
# times=[]
# for i in range(len(data)-1):
# 	times.append(abs(data[i+1][0]-data[i][0])+abs(data[i+1][1]-data[i][1]))
time=0
#print (coor,ind,m)
prev=(sx,sy)
flag=0
count=0
for i in range(ind,-1,-1):
	time+=(abs(data[i][0]-prev[0])+abs(data[i][1]-prev[1]))
	#print (time)
	if time<=t:
		count+=1
		prev=data[i]
	else:
		flag=1
		break
#print (flag)
if flag==1:
	print (count)
else:
	for i in range(ind+1,len(data)):
		time+=(abs(data[i][0]-prev[0])+abs(data[i][1]-prev[1]))
		if time<=t:
			count+=1
			prev=data[i]
		else:
			break
		#print (time)
	print (count)
