n, q, k = map(int,input().split())
a = list(map(int,input().split()))
c = [a[0]-1]
for i in range(1, n-1):
	c.append(a[i+1]-a[i-1]-2)
c.append(k-a[-1]-1)
p = [c[0]]
for i in range(1, n):
	p.append(p[-1]+c[i])
# print (c)
# print (p)
for i in range(q):
	l, r = map(int,input().split())
	if r-l>=2:
		x = p[r-2]-p[l-1]
		x += (k-a[r-2]-1)
		x += (a[l]-2)
		print (x)
	elif r-l==1:
		x = (k-a[r-1]+a[l-1]-1+2*(a[r-1]-a[l-1]-1))
		print (x)
	else:
		print (k-1)


