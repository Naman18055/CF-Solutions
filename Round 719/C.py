for nt in range(int(input())):
	n = int(input())
	if n==1:
		print (1)
		continue
	elif n==2:
		print (-1)
		continue

	ans = [[0 for i in range(n)] for j in range(n)]
	curr = 1
	for i in range(n):
		for j in range(n):
			if (i+j)%2:
				ans[i][j] = curr
				curr += 1
	for i in range(n):
		for j in range(n):
			if ans[i][j]==0:
				ans[i][j] = curr
				curr += 1
	for i in ans:
		print (*i)