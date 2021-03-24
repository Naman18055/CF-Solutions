def check(num):
	if (num**2+1)//2<=n:
		return True
	return False

for nt in range(int(input())):
	n = int(input())
	low = 1
	high = n
	while low<high:
		mid = (low+high)//2
		if not mid%2:
			mid += 1
		if check(mid):
			low = mid + 1
		else:
			high = mid - 1

	# print (low)
	if not low%2:
		if check(low+1):
			print (low//2)
		else:
			print (low//2-1)
	else:
		if check(low):
			print (low//2)
		else:
			print (low//2-1)

