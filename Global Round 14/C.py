for nt in range(int(input())):
	n, m, x = map(int,input().split())
	a = list(map(int,input().split()))
	ans = [0]*n
	arr = []
	for i in range(n):
		arr.append([a[i], i])
	arr.sort()
	for i in range(n):
		ans[arr[i][1]] = i%m + 1
	print ("YES")
	print (*ans)