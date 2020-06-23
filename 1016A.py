n,m=map(int,input().split())
l=list(map(int,input().split()))
ans=[l[0]//m]
s=l[0]
prev=l[0]//m
for i in range(1,n):
	s+=l[i]
	ans.append(s//m-prev)
	prev+=ans[-1]
print (*ans)