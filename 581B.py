n=int(input())
l=list(map(int,input().split()))
if n==1:
	print (0)
	exit()
m=[-1]*n
maxx=l[-1]
m[-2]=maxx
for i in range(n-3,-1,-1):
	maxx=max(maxx,m[i+1],l[i+1])
	m[i]=maxx
ans=[]
# print (m)
for i in range(n):
	if l[i]>m[i]:
		ans.append(0)
	else:
		ans.append((m[i]-l[i]+1))
print (*ans)