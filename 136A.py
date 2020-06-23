n=int(input())
l=list(map(int,input().split()))
d={}
for i in range(n):
	d[l[i]]=i+1
for i in range(1,n+1):
	print (d[i],end=" ")
print ()