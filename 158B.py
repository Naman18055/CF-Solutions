import math
n=int(input())
l=list(map(int,input().split()))
ans=0
ans+=l.count(4)
ans+=l.count(2)//2
left2 = l.count(2)%2
one = l.count(1)
three = l.count(3)
ans+=min(one,three)
if one>three:
	ans+=math.ceil((one-min(one,three)+2*left2)/4)
else:
	ans+=three-min(one,three)+left2
print (ans)

