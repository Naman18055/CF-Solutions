n,m=map(int,input().split())
a=[]
b=[]
for i in range(n):
	x,y=map(int,input().split())
	a.append(x)
	b.append(y)
if sum(b)>m:
	print(-1)
	exit()
if sum(a)<=m:
	print (0)
	exit()
diff=[]
for i in range(n):
	diff.append(a[i]-b[i])
diff.sort(reverse=True)
x=sum(a)
ans=0
while x>m:
	x-=diff[ans]
	ans+=1
print (ans)
