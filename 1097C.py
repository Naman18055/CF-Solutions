from collections import Counter
n=int(input())
l=[]
for i in range(n):
    s=input()
    count,temp=0,0
    for j in s:
        if j=="(":
            count+=1
        else:
            count-=1
        temp=min(temp,count)
    if temp>=min(0,count):
        l.append(count)
c=Counter(l)
ans=0
# print (c)
for i in range(1,300000):
    if i in c:
        if -1*i in c:
            ans+=min(c[i],c[-1*i])
if 0 in c:
    ans+=(c[0]//2)
print (ans)