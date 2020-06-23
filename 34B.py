n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
i=0
ans=0
while i<m and l[i]<0:
	ans+=l[i]
	i+=1
print (ans*-1)