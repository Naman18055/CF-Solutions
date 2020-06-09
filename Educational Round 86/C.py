import math
for nt in range(int(input())):
	a,b,q=map(int,input().split())
	lcm = (a*b)//math.gcd(a,b)
	for i in range(q):
		l,r=map(int,input().split())
		if b%a==0 or a%b==0:
			print (0,end=" ")
			continue
		ans=r-l+1
		m=max(a,b)
		x=l//lcm+1
		y=r//lcm
		ans-=max(0,y-x+1)*m
		i=l
		# print (ans,y,x)
		while ((i%a)%b)==((i%b)%a) and i<=r:
			ans-=1
			i+=1
		j=r+1
		if x<=y and j%lcm!=0:
			while ((j%a)%b)==((j%b)%a):
				ans+=1
				j+=1
		print (ans,end=" ")
	print ()
