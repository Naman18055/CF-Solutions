a,b=map(int,input().split())
s1,s2,s3 = a**0.5,b**0.5,(a+b)**0.5
m = a+b
ans=0
for i in range(1,int(s3)+1):
    if i<=s1 and a%i==0:
        m=min(m,a//i)
    if i<=s2 and b%i==0:
        m=min(m,b//i)

    if (a+b)%i==0:
        d=(a+b)//i
        if d>=m:
            ans=(i+d)*2
 
print (ans)