n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
x=l[-1]-l[1]
y=l[-2]-l[0]
if x>y:
	print (y)
else:
	print (x)