l=list(map(int,input().split()))
s=(l[0]+l[1]+l[2]+l[3])//3
l.remove(max(l))
a=(l[0]+l[1]-l[2])//2
b=l[0]-a
c=l[1]-a
print (a,end=" ")
print (b,end=" ")
print (c,end=" ")
