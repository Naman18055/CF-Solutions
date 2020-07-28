import sys
input = sys.stdin.readline
def check(num):
	count = 0
	prev = 0
	for i in trap:
		if i[2]>num:
			if i[0]<=prev:
				count += max(0,i[1]-prev)
				prev = max(prev,i[1])
			else:
				count += (i[1]-i[0]+1)
				prev = i[1]

	count = (count)*2 + n+1
	if count<=t:
		return True
	return False

m,n,k,t = map(int,input().split())
a = sorted(list(map(int,input().split())))[::-1]
trap = []
for i in range(k):
	trap.append(tuple(map(int,input().split())))
trap.sort()
low = 0
high = m
while low<high:
	mid = (low+high)//2
	if check(a[mid]):
		low = mid + 1
	else:
		high = mid - 1
if low<m and check(a[low]):
	print (low+1)
else:
	print (low)