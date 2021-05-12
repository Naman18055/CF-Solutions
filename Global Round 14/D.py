from collections import Counter
for _ in range(int(input())):
    n,l,r=map(int,input().split())
    s=list(map(int,input().split()))
    s1=s[:l]
    s2=s[l:]
    ans=0
    if len(s1)>len(s2):
        s1,s2=s2,s1
    d=Counter(s2)
    q=Counter(s1)
    for i in q.keys():
        if i in d.keys():
            if d[i]>=q[i]:
                d[i]-=q[i]
            else:
                ans+=q[i]-d[i]
                d[i]=0
        else:
            ans+=q[i]
    t=abs(n//2-l)
    ans+=t
    x=0
    for i in d.keys():
        x+=d[i]//2
    if x<t:
        ans+=t-x
    print(ans)