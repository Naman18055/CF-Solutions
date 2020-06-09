n,k=map(int,input().split())
b=-(2*n+3)
c=(n**2+n-2*k)
ans1=(-b+(b*b-4*c)**(0.5))//2
ans2=(-b-(b*b-4*c)**(0.5))//2
if ans1>=0 and ans1<n:
	print (int(ans1))
else:
	print (int(ans2))