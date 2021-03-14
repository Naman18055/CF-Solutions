for nt in range(int(input())):
	n, k = map(int,input().split())
	a = list(map(int,input().split()))
	b = [a[i] for i in range(n)]
	ans = 0
	for i in range(n-2, -1, -1):
		if a[i]<a[i+1]:
			ans += a[i+1]-a[i]
			a[i] = a[i+1]
	if ans<k:
		print (-1)
		continue

	ans = -1
	while True:
		for i in range(1, n):
			if b[i]>b[i-1]:
				k -= 1
				b[i-1] += 1
				break
		if k<=0:
			ans = i
			break
		# print (k, b)

	print (ans)





