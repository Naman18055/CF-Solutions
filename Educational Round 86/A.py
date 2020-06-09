for nt in range(int(input())):
	x,y=map(int,input().split())
	x2,y2=map(int,input().split())
	ans=0
	ans+=abs(x-y)*x2
	print (ans+min(2*x2*min(x,y),y2*min(x,y)))