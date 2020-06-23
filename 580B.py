import sys
input = sys.stdin.readline
def check(num):
	i,j = 0,0
	count = 0
	while j<n:
		while j<n and (a[j][0]-a[i][0])<d:
			count += a[j][1]
			j += 1
		if count>=num:
			return True
		count -= a[i][1]
		i += 1
	return False


n,d = map(int,input().split())
a = []
maxx = 0
for i in range(n):
	a.append(list(map(int,input().split())))
	maxx += a[-1][1]
a.sort()
if n==1:
	print (a[0][1])
	exit()
low = 0
high = maxx
while low<high:
	mid = (low+high)//2
	if check(mid):
		low = mid+1
	else:
		high = mid-1
if check(low):
	print (low)
else:
	print (low-1)