def check(num):
	c1,c2 = 0,0
	m = n
	while m!=0:
		c1 += min(num,m)
		m -= (min(num,m))
		c2 += m//10
		m -= m//10
	if c1>=((n-1)//2+1):
		return True
	return False

n = int(input())
low = 1
high = n
while low<high:
	mid = (low+high)//2
	if check(mid):
		high = mid - 1
	else:
		low = mid + 1
if check(low):
	print (low)
else:
	print (low+1)