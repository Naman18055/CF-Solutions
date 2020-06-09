import math
n,k=map(int,input().split())
p=list(map(int,input().split()))
a=int(input())
c=list(map(int,input().split()))
l=[]
for i in range(n):
	if k+(i+1)*a<p[i]:
		print (-1)
		exit()
	else:
		l.append(math.ceil((p[i]-k)/a))

