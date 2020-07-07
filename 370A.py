r1,c1,r2,c2 = map(int,input().split())
if (r1+c1)%2!=(r2+c2)%2:
	b = 0
else:
	if abs(r1-r2)==abs(c1-c2):
		b = 1
	else:
		b = 2
if r1==r2 or c1==c2:
	r = 1
else:
	r = 2
x = abs(r1-r2)
y = abs(c1-c2)
k = max(x,y)
print (r,b,k)