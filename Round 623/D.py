
n=int(input())
a=list(map(int,input().split()))
t=list(map(int,input().split()))
new=[]
for i in range(n):
	new.append([a[i],t[i]])
new.sort(reverse=True)
nxt=new[0][0]+1
last=nxt
taken={}
for i in new:
	taken[i[0]]=1
prev=new[0]
prev_cost=0
this_cost=new[0][1]
ans=0
for i in range(1,n):
	if new[i][0]==new[i-1][0]:
		if new[i][0]!=new[0][0]:
			ans+=min(new[i][1]*(nxt-new[i][0]),new[i][1]*(prev[0]-new[i][0])+prev_cost)
		else:
			ans+=new[i][1]*(nxt-new[i][0])
		taken[nxt]=1
		if nxt==last:
			last+=1
			nxt+=1
		else:
			nxt+=1
		if nxt in taken:
			nxt=last
		this_cost+=new[i][1]
	else:
		if new[i][0]!=new[i-1][0]-1:
			nxt=new[i][0]+1
		prev=new[i-1]
		prev_cost+=this_cost
		this_cost=new[i][1]
	print (ans,prev_cost,this_cost,nxt,last)
print (ans)
