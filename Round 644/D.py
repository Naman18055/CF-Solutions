for nt in range(int(input())):
	n, k = map(int,input().split())
	if k>=n:
		print (1)
		continue
	ans = n
	for i in range(1,min(int(n**0.5)+1,k+1)):
		if n%i==0:
			ans = min(ans, n//i)
			if n//i<=k:
				ans = min(ans, i)
	print (ans)