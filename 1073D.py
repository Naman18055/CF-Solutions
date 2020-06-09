import sys
input = sys.stdin.readline

n,t=map(int,input().split())
l=list(map(int,input().split()))
minn=min(l)
ans=0
while t>=minn:
	c=0
	count=0
	for i in l:
		if i<=t:
			count+=i
			t-=i
			c+=1
	t+=count
	# print (t,c,count)
	ans+=c*(t//count)
	t=t%count
print (ans)