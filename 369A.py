n,m,k=map(int,input().split())
l=list(map(int,input().split()))
ans=0
ans+=max(0,l.count(1)-m)
m=max(m-l.count(1),0)
ans+=max(0,l.count(2)-k-m)
print (ans)