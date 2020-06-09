import sys
input = sys.stdin.readline

n=int(input())
l=[[] for i in range(n)]
ans={}
initial=[]
for i in range(n-1):
	a,b=list(map(int,input().split()))
	initial.append((a-1,b-1))
	ans[(a-1,b-1)]=-1
	ans[(b-1,a-1)]=-1
	l[a-1].append(b-1)
	l[b-1].append(a-1)
flag=0
for i in range(len(l)):
	if len(l[i])>2:
		flag=1
		index=i
		break
if flag==0:
	for i in range(n-1):
		print (i)
else:
	for i in range(3):
		ans[(index,l[index][i])]=i
		ans[(l[index][i],index)]=i
	k=3
	#print (ans)
	for i in range(n-1):
		if ans[(initial[i][0],initial[i][1])]==-1:
			print (k)
			k+=1
		else:
			print (ans[(initial[i][0],initial[i][1])])