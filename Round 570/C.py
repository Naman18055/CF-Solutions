t=int(input())
for i in range(t):
	k,n,a,b=map(int,input().split())
	if ((k-(n*b))//(a-b))==((k-(n*b))/(a-b)):
		print (min(n,((k-(n*b))//(a-b))-1))
	else:
		if (k-n*b)<=0:
			print (-1)
		else:
			print (min(n,((k-(n*b))//(a-b))))