from bisect import bisect_left
def calc(a,b):
	c = []
	for i in b:
		for j in i:
			c.append(j)
	c = list(set(c))
	d = []
	for i in range(len(a)):
		for j in a[i]:
			d.append((j,i))
	d.sort()

	ans = 0
	for i in d:
		for j in i:
			x = bisect_left(c,j[0])
			# print (j,c,x)
			ans += (x*(j[1]+1))
	return len(a)*len(b)


def merge(a):
	if len(a)==1:
		return len(a[0])
	else:
		n = len(a)
		x = merge(a[0:n//2])
		y = merge(a[n//2:])
		print (a,x,y,calc(a[0:n//2],a[n//2:]))
		return x + y + calc(a[0:n//2],a[n//2:])


n = int(input())
d = {}
xcoor = []
for i in range(n):
	x,y = map(int,input().split())
	if x not in d:
		d[x] = [y]
	else:
		d[x].append(y)
	xcoor.append(x)
xcoor.sort()

p = []
for i in xcoor:
	p.append(d[i])

print (p)
print (merge(p))
