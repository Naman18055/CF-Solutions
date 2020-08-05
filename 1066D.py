def check(num):
	left = m
	curr = k
	for i in range(n-num,n):
		if curr>=a[i]:
			curr -= a[i]
		else:
			if left==1:
				return False
			left -= 1
			curr = k - a[i]
	return True


n,m,k = map(int,input().split())
a = list(map(int,input().split()))
low = 0
high = n
while low<high:
	mid = (low+high)//2
	if check(mid):
		low = mid + 1
	else:
		high = mid - 1
if check(low):
	print (low)
else:
	print (low-1)