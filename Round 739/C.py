for nt in range(int(input())):
	n = int(input())
	k = int((n-1)**0.5)+1
	j = min(k, k - (k**2 - k + 1 - n))
	i = min(k, k**2 - n + 1)
	print (j, i)