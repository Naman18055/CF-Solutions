for nt in range(int(input())):
	n, k = map(int,input().split())
	diff = n - k + 1
	for i in range(1, k-diff+1):
		print (i, end=" ")
	for i in range(k, k-diff, -1):
		print (i, end=" ")
	print ()