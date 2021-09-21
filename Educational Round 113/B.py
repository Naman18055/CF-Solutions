for nt in range(int(input())):
	n = int(input())
	s = input()
	ans = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		ans[i][i] = "X"

	for i in range(n):
		if s[i]=="1":
			for j in range(n):
				if i!=j:
					ans[i][j] = "="
					ans[j][i] = "="

	final = "YES"
	for i in range(n):
		done = False
		for j in range(n):
			if ans[i][j]!=0:
				if ans[i][j]=="+":
					done = True
				continue
			if not done:
				ans[i][j] = "+"
				ans[j][i] = "-"
				done = True
			else:
				ans[i][j] = "-"
				ans[j][i] = "+"

		if s[i]=="2" and not done:
			final = "NO"
			break

	for i in range(n):
		ans[i][i]="X"

	print (final)
	if final=='YES':
		for i in ans:
			print ("".join(i))


