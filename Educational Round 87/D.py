def check(num):
	x = 0
	for i in a:
		if i<num:
			x += 1
		else:
			break
	y = n-x
	for j in q:
		if j>0:
			if j>=num:
				y += 1
			else:
				x += 1
		else:
			k = abs(j)
			if k<=x:
				x -= 1
			else:
				y -= 1
	# print (num,x,y)
	return x


n,m = map(int,input().split())
a = list(map(int,input().split()))
q = list(map(int,input().split()))
x = 0
for i in q:
	if i<0:
		x += 1
if 2*x==n+m:
	print (0)
	exit()

low = 1
high = n
while low<high:
	mid = (low+high)//2
	if check(mid):
		high = mid-1
	else:
		low = mid+1

if check(low):
	print (low-1)
else:
	print (low)
