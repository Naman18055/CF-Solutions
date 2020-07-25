def check(num):
	m = k
	m -= a*num
	m -= b*(max(0,n-num))
	if m>0:
		return True
	return False



for nt in range(int(input())):
	k,n,a,b = map(int,input().split())
	low = 0
	high = k//a+1
	while low<high:
		mid = (low+high)//2
		if check(mid):
			low = mid + 1
		else:
			high = mid - 1
	if check(low):
		print (min(n,low))
	else:
		print (min(n,low-1))