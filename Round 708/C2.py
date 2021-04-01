for nt in range(int(input())):
	n, k = map(int,input().split())
	ans = [1]*(k-3)
	n -= (k-3)
	if n%2:
		ans.extend([1, n//2, n//2])
	else:
		if n//2%2:
			ans.extend([2, n//2-1, n//2-1])
		else:
			ans.extend([n//2, n//4, n//4])
	print (*ans)