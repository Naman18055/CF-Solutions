def bs(num):
	low = 0
	high = b-1
	while low<high:
		mid = (low+high)//2
		if l[mid][0]<=num:
			low = mid + 1
		else:
			high = mid - 1
	if l[low][0]<=num:
		return low
	else:
		return low-1

n,b = map(int,input().split())
a = list(map(int,input().split()))
l = []
for i in range(b):
	l.append(list(map(int,input().split())))
l.sort()
p = [l[0][1]]
for i in range(1,b):
	p.append(p[-1]+l[i][1])

for i in a:
	pos = bs(i)
	if pos==-1:
		print (0,end=" ")
	else:
		print (p[pos],end=" ")
print ()