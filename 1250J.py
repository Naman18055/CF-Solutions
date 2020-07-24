def check(num):
	if num==0:
		return True
	x = k
	i = 0
	left = a[0]
	while x>0 and i<n:
		if i==n-1:
			x -= left//num
			break
		s = left+a[i+1]
		x -= s//num
		left = min(a[i+1],s%num)
		i += 1
	if x>0:
		return False
	return True

for nt in range(int(input())):
	n,k = map(int,input().split())
	a = list(map(int,input().split()))
	low = 0
	high = 10**18
	while low<high:
		mid = (low+high)//2
		if check(mid):
			low = mid + 1
		else:
			high = mid - 1
	
	if check(low):
		print (low*k)
	else:
		print ((low-1)*k)