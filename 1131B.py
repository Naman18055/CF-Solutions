n=int(input())
a=0
b=0
ans=1
temp=0
for i in range(n):
	x,y=map(int,input().split())
	if a!=b:
		temp=1
	else:
		temp=0
	if min(x,y)-max(a,b)+temp>=0:
		ans+=min(x,y)-max(a,b)+temp
	a,b=x,y
print(ans)