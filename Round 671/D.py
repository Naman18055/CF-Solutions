def count(arr):
	c = 0
	for i in range(1,len(arr)-1):
		if arr[i]<arr[i-1] and arr[i]<arr[i+1]:
			c += 1
	print (c)

n = int(input())
a = sorted(list(map(int,input().split())))
if n%2:
	ans = [0]*n
	j = 0
	for i in range(1,n,2):
		ans[i] = a[j]
		j += 1
	for i in range(0,n,2):
		ans[i] = a[j]
		j += 1
	count(ans)
	print (*ans)
else:
	ans = [0]*n
	j = 0
	for i in range(1,n,2):
		ans[i] = a[j]
		j += 1
	for i in range(0,n,2):
		ans[i] = a[j]
		j += 1
	count(ans)
	print (*ans)
