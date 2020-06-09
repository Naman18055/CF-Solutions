import sys
input = sys.stdin.readline
for nt in range(1):
	n=int(input())
	l=list(map(int,input().split()))
	q=int(input())
	last={}
	maxx=[0]*q
	t2=[]
	for i in range(q):
		temp=list(map(int,input().split()))
		if temp[0]==1:
			last[temp[1]]=(temp[2],i)
		else:
			t2.append((temp[1],i))
	if len(t2)>0:
		j=len(t2)-1
		m=-1
		for i in range(q-1,-1,-1):
			if i>t2[j][1]:
				maxx[i]=m
			else:
				maxx[i]=max(t2[j][0],m)
				j-=1
				m=maxx[i]
		# print (maxx)
	ans=[]
	for i in range(n):
		if i+1 in last:
			ans.append(max(last[i+1][0],maxx[last[i+1][1]]))
		else:
			ans.append(max(maxx[0],l[i]))
	print (*ans)
