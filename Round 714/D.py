for nt in range(int(input())):
	n, p = map(int,input().split())
	a = list(map(int,input().split()))
	b = [(a[i], i) for i in range(n)]
	b.sort()
	ans = [p]*n
	for i, j in b:
		for k in range(j-1, -1, -1):
			if a[k]%i==0 and ans[k]>i:
				ans[k] = i
			else:
				break
		for k in range(j+1, n):
			if a[k]%i==0 and ans[k-1]>i:
				ans[k-1] = i 
			else:
				break
	print (sum(ans)-p)