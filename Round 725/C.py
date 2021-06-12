def calc(num, ind):
	low = ind
	high = n - 1
	while low<high:
		mid = (low+high)//2
		if a[mid]+num<=r:
			low = mid + 1
		else:
			high = mid - 1
	if low<n and a[low]+num<=r:
		v1 = low
	else:
		v1 = low - 1
	low = ind
	high = n-1
	while low<high:
		# print (low, high)
		mid = (low+high)//2
		if a[mid]+num<l:
			low = mid + 1
		else:
			high = mid - 1
	# print (low, high)
	if low<n and a[low]+num>=l:
		v2 = low
	else:
		v2 = low + 1
	# print (ind)
	# print(v1, v2)
	return max(0, v1 - v2 + 1)


for nt in range(int(input())):
	n, l, r = map(int,input().split())
	a = list(map(int,input().split()))
	a.sort()
	ans = 0
	for i in range(n):
		ans += calc(a[i], i+1)
	print (ans)



