def bs(num):
	low = 0
	high = m-1
	while low<high:
		mid = (low+high)//2
		if b[mid]>num:
			high = mid - 1
		elif b[mid]==num:
			return 0
		else:
			low = mid + 1
	if b[low]>num:
		if low==0:
			return abs(b[low]-num)
		low -= 1
	if low+1>=m:
		return abs(b[low]-num)
	return min(abs(b[low]-num),abs(b[low+1]-num))

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
b.sort()
ans = 0
for i in range(n):
	ans = max(ans, bs(a[i]))
	# print (ans,bs(a[i]))
print (ans)