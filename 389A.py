import math
n=int(input())
l=list(map(int,input().split()))
ans=l[0]
for i in range(1,n):
	ans=math.gcd(ans,l[i])
print (ans*n)