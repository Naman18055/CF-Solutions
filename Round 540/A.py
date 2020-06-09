t=int(input())
for i in range(t):
	n,a,b = map(int,input().split())
	x=n
	p1=n*a
	if n%2==0:
		y=n//2
		p2=y*b
	else:
		y=n//2
		p2=y*b+a
	print (min(p1,p2))