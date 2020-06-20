n,m = map(int,input().split())
if m==0:
	print (n,n)
	exit()

ans = n-2*m
print (max(ans,0),end = " ")
c = 2
while ((c*(c-1))//2)<m:
	c += 1
print (n-c)