k,b,n,t=map(int,input().split())
x=1
while x<=t:
	x,n=x*k+b,n-1
print (max(0,n+1))