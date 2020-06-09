from collections import deque
n,q=map(int,input().split())
l=list(map(int,input().split()))
# new=[]
# for i in range(n):
# 	temp=l[i]
# 	new.append(temp)
new=deque(l)
comp=[]
comp.append(new.popleft())
temp=max(l)
ans=[]
while comp[0]!=temp:
	ans.append((comp[0],new[0]))
	if comp[0]<new[0]:
		new.append(comp.pop())
		comp.append(new.popleft())
	else:
		new.append(new.popleft())
for i in range(q):
	query=int(input())
	if query<=len(ans):
		print (ans[query-1][0],end=" ")
		print (ans[query-1][1])
	else:
		temp2=query-len(ans)-1
		print (temp,end=" ")
		print (new[temp2%(n-1)])
